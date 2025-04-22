import random
from data import (
    FIGHTER_ABILITIES, PALADIN_ABILITIES, SORCERER_ABILITIES,
    CLERIC_ABILITIES, RANGER_ABILITIES, ENCOUNTERS, BOSS_ENCOUNTER
)

class Character:
    def __init__(self, name, stats, max_hp):
        self.name = name
        self.stats = stats
        self.max_hp = max_hp
        self.hp = max_hp
        self.active_effects = []

class Player(Character):
    def __init__(self, name, class_name, stats, level=1, xp=0):
        self.class_name = class_name
        abilities = self.load_abilities(class_name)
        max_hp = 100 + stats.get("CON", 0) * 10
        super().__init__(name, stats, max_hp)
        self.level = level
        self.xp = xp
        self.abilities = abilities

    def load_abilities(self, class_name):
        return {
            "Fighter": FIGHTER_ABILITIES,
            "Paladin": PALADIN_ABILITIES,
            "Sorcerer": SORCERER_ABILITIES,
            "Cleric": CLERIC_ABILITIES,
            "Ranger": RANGER_ABILITIES
        }.get(class_name, [])

    def gain_xp(self, amount):
        from constants import LEVEL_CAP, XP_PER_LEVEL
        self.xp += amount
        while self.level < LEVEL_CAP and self.xp >= self.level * XP_PER_LEVEL:
            self.xp -= self.level * XP_PER_LEVEL
            self.level += 1
            self.max_hp += 10
            self.hp = self.max_hp
            self.stats["STR"] += 1

    @staticmethod
    def from_save(data):
        return Player(
            data["name"],
            data["class"],
            data["stats"],
            data.get("level", 1),
            data.get("xp", 0)
        )

class Enemy(Character):
    def __init__(self, index):
        if index >= 4:
            info = BOSS_ENCOUNTER
        else:
            info = ENCOUNTERS[index]
        stats = {"STR": 5, "INT": 3, "DEX": 2, "CON": 4, "LCK": 1}
        super().__init__(info["name"], stats, info["hp"])
        self.abilities = info["moves"]

    def choose_move(self):
        return random.choice(self.abilities)
