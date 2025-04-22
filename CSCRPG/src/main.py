import pygame
import json
import os
from constants import *
from screens import StartScreen, ClassSelectionScreen, StatAllocationScreen, CombatScreen, VictoryScreen
from characters import Player

def load_save():
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r") as f:
            return json.load(f)
    return None

def save_game(player, current_battle):
    save_data = {
        "name": player.name,
        "class": player.class_name,
        "stats": player.stats,
        "level": player.level,
        "xp": player.xp,
        "current_battle": current_battle
    }
    with open("save_data.json", "w") as f:
        json.dump(save_data, f)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("CSC RPG v1.3.0")
    clock = pygame.time.Clock()

    save_data = load_save()
    start_screen = StartScreen(screen, save_data)
    selected_option = start_screen.run()

    if selected_option == "continue":
        player = Player.from_save(save_data)
        current_battle = save_data.get("current_battle", 0)
    else:
        class_select = ClassSelectionScreen(screen)
        class_choice = class_select.run()
        stat_alloc = StatAllocationScreen(screen, class_choice)
        player = stat_alloc.run()
        current_battle = 0

    while current_battle < 4:
        combat = CombatScreen(screen, player, current_battle)
        result = combat.run()

        if result == "victory":
            player.gain_xp(100)
            current_battle += 1
            save_game(player, current_battle)
            if current_battle < 4:
                victory = VictoryScreen(screen, player, win=True)
                victory.run()
        else:
            victory = VictoryScreen(screen, player, win=False)
            victory.run()
            current_battle = 0
            if os.path.exists("save_data.json"):
                os.remove("save_data.json")

    if current_battle >= 4:
        victory = VictoryScreen(screen, player, win=True, final=True)
        victory.run()
        if os.path.exists("save_data.json"):
            os.remove("save_data.json")

    pygame.quit()

if __name__ == "__main__":
    main()
