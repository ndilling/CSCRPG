import pygame
import random
from constants import *
from data import ABILITIES, STAT_NAMES
from characters import Player, Enemy
from gui_utils import draw_text, draw_bar, draw_tooltip, draw_combat_log
from tooltips import STAT_TOOLTIPS, CLASS_TOOLTIPS

class StartScreen:
    def __init__(self, surface, save_exists):
        self.surface = surface
        self.save_exists = save_exists
        self.font = pygame.font.SysFont(None, FONT_LARGE)

    def run(self):
        running = True
        while running:
            self.surface.fill(BLACK)
            draw_text(self.surface, "CSC RPG", 300, 100, self.font)
            draw_text(self.surface, "[N] New Game", 300, 200, self.font)
            if self.save_exists:
                draw_text(self.surface, "[C] Continue", 300, 250, self.font)
            draw_text(self.surface, "[Q] Quit", 300, 300, self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        return "new"
                    if event.key == pygame.K_c and self.save_exists:
                        return "continue"
                    if event.key == pygame.K_q:
                        return "quit"

            pygame.display.flip()

class ClassSelectionScreen:
    def __init__(self, surface):
        self.surface = surface
        self.classes = list(CLASS_TOOLTIPS.keys())
        self.font = pygame.font.SysFont(None, FONT_MEDIUM)
        self.tooltip_font = pygame.font.SysFont(None, FONT_SMALL)

    def run(self):
        selected = None
        while not selected:
            self.surface.fill(BLACK)
            mouse = pygame.mouse.get_pos()
            for i, class_name in enumerate(self.classes):
                rect = pygame.Rect(100, 100 + i*60, 300, 50)
                pygame.draw.rect(self.surface, GRAY, rect)
                draw_text(self.surface, class_name, rect.x + 10, rect.y + 10, self.font)
                if rect.collidepoint(mouse):
                    draw_tooltip(self.surface, CLASS_TOOLTIPS[class_name], mouse, self.tooltip_font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Fighter"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, class_name in enumerate(self.classes):
                        if pygame.Rect(100, 100 + i*60, 300, 50).collidepoint(mouse):
                            selected = class_name

            pygame.display.flip()
        return selected

class StatAllocationScreen:
    def __init__(self, surface, class_choice):
        self.surface = surface
        self.class_choice = class_choice
        self.font = pygame.font.SysFont(None, FONT_MEDIUM)
        self.tooltip_font = pygame.font.SysFont(None, FONT_SMALL)
        self.stats = {k: 1 for k in STAT_NAMES}
        self.points = 20

    def run(self):
        confirmed = False
        while not confirmed:
            self.surface.fill(BLACK)
            mouse = pygame.mouse.get_pos()
            draw_text(self.surface, f"Points left: {self.points}", 100, 50, self.font)
            for i, stat in enumerate(STAT_NAMES):
                y = 100 + i*50
                draw_text(self.surface, f"{stat}: {self.stats[stat]}", 100, y, self.font)
                plus_rect = pygame.Rect(300, y, 30, 30)
                pygame.draw.rect(self.surface, GREEN, plus_rect)
                draw_text(self.surface, "+", plus_rect.x + 5, plus_rect.y, self.font)
                if plus_rect.collidepoint(mouse):
                    draw_tooltip(self.surface, STAT_TOOLTIPS[stat], mouse, self.tooltip_font)

            confirm_rect = pygame.Rect(100, 400, 200, 50)
            pygame.draw.rect(self.surface, BLUE, confirm_rect)
            draw_text(self.surface, "Confirm", 120, 410, self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, stat in enumerate(STAT_NAMES):
                        if pygame.Rect(300, 100 + i*50, 30, 30).collidepoint(mouse):
                            if self.points > 0:
                                self.stats[stat] += 1
                                self.points -= 1
                    if confirm_rect.collidepoint(mouse) and self.points == 0:
                        confirmed = True

            pygame.display.flip()
        return Player("Hero", self.class_choice, self.stats)

class CombatScreen:
    def __init__(self, surface, player, encounter_index):
        self.surface = surface
        self.player = player
        self.enemy = Enemy(encounter_index)
        self.font = pygame.font.SysFont(None, FONT_SMALL)
        self.cooldowns = {a["name"]: 0 for a in self.player.abilities}
        self.log = []
        self.player_turn = True

    def apply_effects(self, target):
        messages = []
        for effect in list(target.active_effects):
            effect["duration"] -= 1
            if effect["type"] in ["burn", "bleed"]:
                dmg = effect["value"]
                target.hp = max(0, target.hp - dmg)
                messages.append(f"{target.name} suffers {dmg} from {effect['type']}!")
            if effect["duration"] <= 0:
                target.active_effects.remove(effect)
        return messages

    def run(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            self.surface.fill(BLACK)
            mouse = pygame.mouse.get_pos()

            # Draw player
            draw_text(self.surface, f"{self.player.name} HP: {self.player.hp}/{self.player.max_hp}", 50, 10, self.font)
            draw_bar(self.surface, 50, 30, 200, 20, self.player.hp, self.player.max_hp, GREEN)

            # Draw enemy
            draw_text(self.surface, f"{self.enemy.name} HP: {self.enemy.hp}/{self.enemy.max_hp}", 50, 60, self.font)
            draw_bar(self.surface, 50, 80, 200, 20, self.enemy.hp, self.enemy.max_hp, RED)

            # Show spell buttons
            buttons = []
            for i, spell in enumerate(self.player.abilities):
                rect = pygame.Rect(50, 120 + i*45, 300, 40)
                pygame.draw.rect(self.surface, GRAY, rect)
                cd = self.cooldowns[spell["name"]]
                draw_text(self.surface, f"{spell['name']} (CD: {cd})", rect.x + 10, rect.y + 5, self.font)
                if rect.collidepoint(mouse):
                    draw_tooltip(self.surface, spell.get("desc", "No description."), mouse, self.font)
                buttons.append((rect, spell))

            # Show combat log
            draw_combat_log(self.surface, self.log, self.font, LOG_AREA_X, LOG_AREA_Y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "defeat"
                if event.type == pygame.MOUSEBUTTONDOWN and self.player_turn:
                    for rect, spell in buttons:
                        if rect.collidepoint(mouse) and self.cooldowns[spell["name"]] == 0:
                            dmg = random.randint(spell["min"], spell["max"])
                            stat_bonus = self.player.stats["STR"]
                            if spell["name"] in ["Fireball", "Magic Missile", "Witch Bolt"]:
                                stat_bonus = self.player.stats["INT"]
                            total_dmg = dmg + stat_bonus

                            if "target" in spell and spell["target"] == "self":
                                self.player.hp = min(self.player.max_hp, self.player.hp + total_dmg)
                                self.log.append(f"{self.player.name} heals for {total_dmg}!")
                            else:
                                self.enemy.hp = max(0, self.enemy.hp - total_dmg)
                                self.log.append(f"{self.player.name} used {spell['name']} for {total_dmg}!")

                                if "effect" in spell:
                                    effect = spell["effect"]
                                    self.enemy.active_effects.append(dict(effect))
                                    self.log.append(f"{self.enemy.name} is afflicted by {effect['type']}!")

                            self.cooldowns[spell["name"]] = spell["cooldown"]
                            self.player_turn = False

            if not self.player_turn and self.enemy.hp > 0:
                self.log += self.apply_effects(self.enemy)
                if any(e["type"] == "stun" for e in self.enemy.active_effects):
                    self.log.append(f"{self.enemy.name} is stunned and skips a turn!")
                else:
                    move = self.enemy.choose_move()
                    dmg = random.randint(move["min"], move["max"])
                    self.player.hp = max(0, self.player.hp - dmg)
                    self.log.append(f"{self.enemy.name} used {move['name']} for {dmg}!")
                self.log += self.apply_effects(self.player)
                for k in self.cooldowns:
                    if self.cooldowns[k] > 0:
                        self.cooldowns[k] -= 1
                self.player_turn = True

            pygame.display.flip()
        return "victory" if self.player.hp > 0 else "defeat"

class VictoryScreen:
    def __init__(self, surface, player, win=True, final=False):
        self.surface = surface
        self.font = pygame.font.SysFont(None, FONT_MEDIUM)
        self.win = win
        self.final = final
        self.player = player

    def run(self):
        timer = 0
        while timer < 180:
            self.surface.fill(BLACK)
            msg = "Victory!" if self.win else "Defeat..."
            if self.final:
                msg = "You defeated the Dark Overlord!"
            draw_text(self.surface, msg, 250, 250, self.font)
            pygame.display.flip()
            pygame.time.delay(20)
            timer += 1
