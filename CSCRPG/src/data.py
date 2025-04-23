STAT_NAMES = ["STR", "INT", "DEX", "CON", "LCK"]

FIGHTER_ABILITIES = [
    {"name": "Burning Hands", "min": 6, "max": 18, "cooldown": 1, "desc": "Close-range flame burst.", "effect": {"type": "burn", "value": 3, "duration": 2}},
    {"name": "Thunderwave", "min": 4, "max": 14, "cooldown": 2, "desc": "Stunning melee wave.", "effect": {"type": "stun", "value": 0, "duration": 1}},
]

PALADIN_ABILITIES = [
    {"name": "Smite Evil", "min": 8, "max": 20, "cooldown": 2, "desc": "Holy strike that burns undead.", "effect": {"type": "burn", "value": 2, "duration": 3}},
    {"name": "Lay on Hands", "min": 10, "max": 18, "cooldown": 2, "desc": "Restore health.", "target": "self"},
]

SORCERER_ABILITIES = [
    {"name": "Fireball", "min": 10, "max": 25, "cooldown": 2, "desc": "Long-range AOE burn.", "effect": {"type": "burn", "value": 5, "duration": 2}},
    {"name": "Witch Bolt", "min": 8, "max": 20, "cooldown": 1, "desc": "Lightning tether."},
]

CLERIC_ABILITIES = [
    {"name": "Cure Wounds", "min": 12, "max": 20, "cooldown": 1, "desc": "Heals moderate damage.", "target": "self"},
    {"name": "Turn Undead", "min": 10, "max": 22, "cooldown": 2, "desc": "Blasts undead enemies with divine light."},
]

RANGER_ABILITIES = [
    {"name": "Piercing Shot", "min": 6, "max": 16, "cooldown": 0, "desc": "Ranged arrow that may bleed.", "effect": {"type": "bleed", "value": 2, "duration": 3}},
    {"name": "Multi Shot", "min": 4, "max": 12, "cooldown": 1, "desc": "Fires two quick arrows."},
]

ENCOUNTERS = [
    {"name": "Goblin", "hp": 90, "moves": [{"name": "Stab", "min": 13, "max": 18, "cooldown": 0}]},
    {"name": "Skeleton", "hp": 100, "moves": [{"name": "Bone Slash", "min": 14, "max": 20, "cooldown": 1}]},
    {"name": "Orc", "hp": 130, "moves": [{"name": "Club Smash", "min": 16, "max": 23, "cooldown": 2}]},
    {"name": "Dark Knight", "hp": 250, "moves": [{"name": "Dark Slash", "min": 17, "max": 23, "cooldown": 2}]}
]

BOSS_ENCOUNTER = {
    "name": "Demon Lord",
    "hp": 160,
    "moves": [
        {"name": "Hellfire", "min": 12, "max": 22, "cooldown": 2, "effect": {"type": "burn", "value": 4, "duration": 3}},
        {"name": "Crush", "min": 10, "max": 18, "cooldown": 2}
    ]
}

# Optional universal mapping if needed elsewhere
ABILITIES = {
    "Burning Hands": FIGHTER_ABILITIES[0],
    "Thunderwave": FIGHTER_ABILITIES[1],
    "Smite Evil": PALADIN_ABILITIES[0],
    "Lay on Hands": PALADIN_ABILITIES[1],
    "Fireball": SORCERER_ABILITIES[0],
    "Witch Bolt": SORCERER_ABILITIES[1],
    "Cure Wounds": CLERIC_ABILITIES[0],
    "Turn Undead": CLERIC_ABILITIES[1],
    "Piercing Shot": RANGER_ABILITIES[0],
    "Multi Shot": RANGER_ABILITIES[1],
}
