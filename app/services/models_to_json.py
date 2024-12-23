def deadly_attacks_to_json(deadly_attacks):
    deadly_attacks_list = [
        {
            "attack_type1": attack.attack_type1,
            "attack_type2": attack.attack_type2,
            "attack_type3": attack.attack_type3,
            "summary": attack.summary,
            "total_score": attack.total_score,
        }
        for attack in deadly_attacks
    ]
    return deadly_attacks_list
