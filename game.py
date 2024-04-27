# Jesus Ortega
# Main Game File for Spell Game
# 04-21-24
import pygame
import Grimoire
from pygame.locals import *
pygame.init()

dark_grimoire = Grimoire.BattleGrimoire(
    "Dark Grimoire", "dark", False, "", 299, 0, 0)

dark_grimoire.effect()
dark_grimoire.attack()

# pygame setup
# pygame.display.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption('CAMGOC')

# Create the main spell library - all grimoires in game
grim_library = []

# opening my grimoire library file
grim_lib_file = open('camgoc-dev\list_of_grims.txt', 'r')
while True:
    # get line from file
    line = grim_lib_file.readline()
    grim_data = []
    # if line is empty
    # end of file is reached
    if not line:
        break

    # print(line.split(',')) - vvv here we are storing the current line into our grimoir data array, we are storing the words in the line in different indecis seperated by a comma
    grim_data = line.split(',')
    # creating new Grimoire object and storing it in a grimoir variable. We fill the object parameters with the grim data array
    grimoire = Grimoire.BattleGrimoire(
        grim_data[0], grim_data[1], False, grim_data[2], grim_data[3], grim_data[4], grim_data[5])
    print(grimoire.name + ": Atk: {}, Type: {}, Heal: {}, Text: {}".format(
        grimoire.attack_points, grimoire.type, grimoire.healing_points, grimoire.effect_text))
    grim_library.append(grimoire)
grim_lib_file.close()

print("MY LIBRARY:")
print("Name:\tAtk:\tEffect:")
for x in grim_library:
    print("{}\t{}\t{}".format(
        x.name, x.attack_points, x.effect_text))

fieldTest = Grimoire.FieldGrimoire('blaj', "fire", True, "", 0)
print(fieldTest.name, fieldTest.type)
# Tables - aka Battles - This will be where the battle state/phases are. ##Draw,play,battle,

# game loop
while running:
    # if user presses x on windoe quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


def _battle(player1, player2):
    # while the battle is active, repeat the Main - End Phases.
    is_active = True

    while is_active:
        # Draw Phase

        # Play Phase

        # Battle Phase

        # End Phase
        if not is_active:
            break
