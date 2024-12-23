import folium
import os

from app.services.country_cordinates import get_country_coordinates

attacks_by_region_map_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'attacks_by_region.html')
attacks_percentage_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'attacks_percentage.html')
most_active_groups_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'most_active_groups.html')
same_target_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'same_target.html')
high_groups_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'high_groups.html')
wide_influence_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'wide_influence.html')
same_strartegys_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'same_strartegy.html')



def attacks_by_region_to_map(attacks_by_regions):
    # חילוץ נקודת ההתחלה
    initial_location = [attacks_by_regions[0]["coordinates"][0]["lat"], attacks_by_regions[0]["coordinates"][0]["lon"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for attack in attacks_by_regions:
        if len(attack['coordinates']) > 5:
            attack['coordinates'] = attack['coordinates'][0:5]
        for coord in attack['coordinates']:
            if coord["lat"] is not None and coord["lon"] is not None:  # בדיקה אם הקורדינטות תקינות
                cords = (coord['lat'], coord['lon'])
                folium.Marker(cords, popup=f'num_attacks: {attack["num_attacks"]}, region:{attack["region"]}, '
                                           f'total_score: {attack["total_score"]}').add_to(map)

    map.save(attacks_by_region_map_path)


def attacks_percentage_to_map(attacks_percentages):
    # חילוץ נקודת ההתחלה
    initial_location = [attacks_percentages[0]["coordinates"][0]["latitude"],
                        attacks_percentages[0]["coordinates"][0]["longitude"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for attack in attacks_percentages:
        if len(attack['coordinates']) > 5:
            attack['coordinates'] = attack['coordinates'][0:5]
        for coord in attack['coordinates']:
            if coord["latitude"] is not None and coord["longitude"] is not None:  # בדיקה אם הקורדינטות תקינות
                cords = (coord['latitude'], coord['longitude'])
                folium.Marker(cords,
                              popup=f'region: {attack["region"]}, num_attacks_start_year: {attack["num_attacks_start_year"]}, num_attacks_end_year:{attack["num_attacks_end_year"]}, '
                                    f'percentage_change: {attack["percentage_change"]}%').add_to(map)

    map.save(attacks_percentage_path)


def most_active_groups_to_map(most_active_groups: dict):
    # חילוץ נקודת ההתחלה
    initial_location = [most_active_groups["Australasia & Oceania"][0]["coordinates"]["latitude"],
                        most_active_groups["Australasia & Oceania"][0]["coordinates"]["longitude"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for region_name, region_value in most_active_groups.items():
        if len(region_value) > 5:
            region_value = region_value[0:5]
        for group in region_value:
            group_lat = group['coordinates']["latitude"]
            group_lon = group['coordinates']["longitude"]
            if group_lat is not None and group_lon is not None:  # בדיקה אם הקורדינטות תקינות
                cords = (group_lat, group_lon)
                folium.Marker(cords,
                              popup=f'region: {region_name}, group_name: {group["group_name"]}, '
                                    f'num_attacks: {group["num_attacks"]}').add_to(map)

    map.save(most_active_groups_path)


# 11

def groups_with_same_target_to_mup(same_targets):
    # חילוץ נקודת ההתחלה
    initial_location = get_country_coordinates(same_targets[0]["country"])
    map = folium.Map(location=initial_location)

    for target in same_targets:
        coordinates = get_country_coordinates(target["country"])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'groups: {target['groups']}, \n type: {target['type']}').add_to(map)

    map.save(same_target_path)


# 14

def same_strartegy_to_mup(same_strartegys):

    # חילוץ נקודת ההתחלה
    initial_location = get_country_coordinates(same_strartegys[0]["country"])
    map = folium.Map(location=initial_location)

    for target in same_strartegys:
        coordinates = get_country_coordinates(target["country"])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'groups: {target['groups']}, \n target: {target['target']}').add_to(map)

    map.save(same_strartegys_path)

# 16
def high_groups_to_mup(high_groups):

    # חילוץ נקודת ההתחלה
    initial_location = get_country_coordinates(high_groups[0]["countries"][0]['name'])
    map = folium.Map(location=initial_location)

    for group in high_groups:
        for country in group['countries']:
            coordinates = get_country_coordinates(country['name'])
            if coordinates and coordinates[0] and coordinates[1]:
                folium.Marker(coordinates,
                              popup=f'country_count: {group['country_count']}, \n group: {group['group']}, \n '
                                    f'target_count: {group['target_count']}, \n type_c'
                                    f'ount: {group['type_count']}').add_to(map)

    map.save(high_groups_path)


# 18
def groups_with_wide_influence_to_mup(wide_influences):

    # חילוץ נקודת ההתחלה
    initial_location = get_country_coordinates(wide_influences[0]["country"])
    map = folium.Map(location=initial_location)

    for country in wide_influences:
        coordinates = get_country_coordinates(country['country'])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'group_count: {country['group_count']}, \n groups: {country['groups']},').add_to(map)

    map.save(wide_influence_path)


