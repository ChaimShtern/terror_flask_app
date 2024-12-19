from app.models import Attack, Casualty, Group, Location
from app.models.attack_group_bridge_model import attack_group_association
from sqlalchemy import func


# 1
def most_deadly_attacks(session_maker):
    with session_maker() as session:
        deadly_attacks = (
            session.query(
                Attack.attack_type1,
                Attack.attack_type2,
                Attack.attack_type3,
                Attack.summary,
                func.sum((Casualty.killed * 2) + Casualty.wounded).label("total_score"),
            )
            .join(Casualty, Attack.id == Casualty.attack_id)
            .group_by(
                Attack.id,
                Attack.attack_type1,
                Attack.attack_type2,
                Attack.attack_type3,
                Attack.summary
            )
            .order_by(func.sum((Casualty.killed * 2) + Casualty.wounded).desc())
            .all()
        )

    if deadly_attacks:
        return deadly_attacks
    else:
        print("Error: deadly_attacks not found")
        return []


# 3
def most_attacked_groups(session_maker):
    with session_maker() as session:
        group_attacks = (
            session.query(
                Group.name.label("group_name"),
                func.count(Attack.id).label("num_attacks"),
                func.sum((Casualty.killed * 2) + Casualty.wounded).label("total_score"),
            )
            .join(attack_group_association, Group.id == attack_group_association.c.group_id)
            .join(Attack, attack_group_association.c.attack_id == Attack.id)
            .join(Casualty, Attack.id == Casualty.attack_id)
            .group_by(Group.id, Group.name)
            .order_by(func.sum((Casualty.killed * 2) + Casualty.wounded).desc())
            .all()
        )

    if group_attacks:
        group_attacks_list = [
            {
                "group_name": group_name,
                "num_attacks": num_attacks,
                "total_score": total_score,
            }
            for group_name, num_attacks, total_score in group_attacks
        ]
        return group_attacks_list
    else:
        print("Error: No data found")
        return []


# 2
def attacks_by_region(session_maker):
    with session_maker() as session:
        region_data = (
            session.query(
                Location.region.label("region"),
                Location.latitude.label("lat"),
                Location.longitude.label("lon"),
                func.count(Attack.id).label("num_attacks"),
                func.sum((Casualty.killed * 2) + Casualty.wounded).label("total_score"),
            )
            .join(Attack, Location.id == Attack.location_id)
            .join(Casualty, Attack.id == Casualty.attack_id)
            .group_by(Location.region, Location.latitude, Location.longitude)
            .order_by(func.sum((Casualty.killed * 2) + Casualty.wounded).desc())
            .all()
        )

    if region_data:
        # ארגון הנתונים כך שכל אזור יקבל רשימת נקודות ציון
        grouped_region_data = {}
        for region, lat, lon, num_attacks, total_score in region_data:
            if region not in grouped_region_data:
                grouped_region_data[region] = {
                    "coordinates": [],
                    "num_attacks": 0,
                    "total_score": 0,
                }
            grouped_region_data[region]["coordinates"].append({"lat": lat, "lon": lon})
            grouped_region_data[region]["num_attacks"] += num_attacks
            grouped_region_data[region]["total_score"] += total_score

        # המרת הנתונים לפורמט רשימה של מילונים
        region_data_list = [
            {
                "region": region,
                "coordinates": data["coordinates"],
                "num_attacks": data["num_attacks"],
                "total_score": data["total_score"],
            }
            for region, data in grouped_region_data.items()
        ]

        return region_data_list
    else:
        print("Error: No data found")
        return []


# 6
def get_attacks_by_year(session, year):
    """
    מחזיר את מספר הפיגועים לפי אזור ונקודות ציון לשנה מסוימת.
    """
    return (
        session.query(
            Location.region.label("region"),
            Location.latitude.label("latitude"),
            Location.longitude.label("longitude"),
            func.count(Attack.id).label("num_attacks")
        )
        .join(Attack, Location.id == Attack.location_id)
        .filter(Attack.year == year)
        .group_by(Location.region, Location.latitude, Location.longitude)
        .all()
    )


# 6
def organize_region_data(attacks_data, key_name, region_data=None):
    """
    מארגן את המידע לפי אזור, כולל קואורדינטות ומספר פיגועים לשנה מסוימת.
    """

    if region_data is None:
        region_data = {}
    for region, latitude, longitude, num_attacks in attacks_data:
        if region not in region_data:
            region_data[region] = {
                "coordinates": [],
                "start_year": 0,
                "end_year": 0
            }
        region_data[region]["coordinates"].append({"latitude": latitude, "longitude": longitude})
        region_data[region][key_name] += num_attacks
    return region_data


# 6
def calculate_percentage_change(region_data):
    """
    מחשב את אחוז השינוי במספר הפיגועים עבור כל אזור.
    """
    results = []
    for region, data in region_data.items():
        num_attacks_start_year = data["start_year"]
        num_attacks_end_year = data["end_year"]

        if num_attacks_start_year > 0:
            change_percentage = ((num_attacks_end_year - num_attacks_start_year) / num_attacks_start_year) * 100
        else:
            change_percentage = 0

        results.append({
            "region": region,
            "coordinates": data["coordinates"],
            "num_attacks_start_year": num_attacks_start_year,
            "num_attacks_end_year": num_attacks_end_year,
            "percentage_change": change_percentage
        })
    return results


# 6
def attacks_percentage_change_by_region(session_maker, start_year, end_year):
    """
    פונקציה מרכזית שמחזירה את אחוז השינוי במספר הפיגועים לפי אזור.
    """
    with session_maker() as session:
        # שליפת נתונים עבור כל שנה
        attacks_period_1 = get_attacks_by_year(session, start_year)
        attacks_period_2 = get_attacks_by_year(session, end_year)
    print(attacks_period_1, attacks_period_2)

    # ארגון המידע לפי אזור
    region_start_data = organize_region_data(attacks_period_1, "start_year")
    region_end_data = organize_region_data(attacks_period_2, "end_year", region_start_data)

    # חישוב אחוז השינוי
    return calculate_percentage_change(region_end_data)


# 8
def most_active_groups_by_region(session_maker):
    with session_maker() as session:
        active_groups_by_region = (
            session.query(
                Location.region.label("region"),
                Group.name.label("group_name"),
                func.count(Attack.id).label("num_attacks"),
                Location.latitude.label("latitude"),
                Location.longitude.label("longitude"),
            )
            .join(Attack, Location.id == Attack.location_id)
            .join(attack_group_association, Attack.id == attack_group_association.c.attack_id)
            .join(Group, Group.id == attack_group_association.c.group_id)
            .group_by(Location.region, Group.name, Location.latitude, Location.longitude)
            .order_by(Location.region, func.count(Attack.id).desc())
            .all()
        )

    # ארגון המידע כך שכל אזור יכיל את הקבוצות הכי פעילות ונקודות הציון שלהן
    region_groups = {}
    for region, group_name, num_attacks, latitude, longitude in active_groups_by_region:
        if region not in region_groups:
            region_groups[region] = []
        region_groups[region].append({
            "group_name": group_name,
            "num_attacks": num_attacks,
            "coordinates": {"latitude": latitude, "longitude": longitude},
        })

    return region_groups
