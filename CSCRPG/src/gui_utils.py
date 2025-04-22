import pygame
from constants import *

def draw_text(surface, text, x, y, font, color=WHITE):
    label = font.render(text, True, color)
    surface.blit(label, (x, y))

def draw_bar(surface, x, y, w, h, current, max_value, color):
    pygame.draw.rect(surface, GRAY, (x, y, w, h))
    fill = int(w * (current / max_value))
    pygame.draw.rect(surface, color, (x, y, fill, h))
    pygame.draw.rect(surface, WHITE, (x, y, w, h), 2)

def draw_tooltip(surface, text, pos, font):
    tooltip_surf = font.render(text, True, WHITE)
    tooltip_rect = tooltip_surf.get_rect()
    tooltip_rect.topleft = (pos[0] + 12, pos[1] + 12)
    pygame.draw.rect(surface, BLACK, tooltip_rect.inflate(8, 6))
    surface.blit(tooltip_surf, tooltip_rect)

def draw_combat_log(surface, log_lines, font, x, y, max_lines=5):
    recent = log_lines[-max_lines:]
    for i, line in enumerate(recent):
        draw_text(surface, line, x, y + i * 20, font)
