# -*- coding: utf-8 -*-
import os
import curses
import os.path
import sys
import pickle
import Undergrounds
import Members
import Functions
import platform
from generator_map import generator, mapsgen
from Draw_Images import draw, rysuj_oddo
from config import Version


# file path for save data
PIK = "save/objects.bj"


def main_menu():
    """Displays the main menu and handles user input."""

    # start and end positions of the menu
    start_position = 0
    end_position = 5

    # menu options with their corresponding functions
    menu_options = {
        0: start_new_game,  # start a new game
        6: load_game,  # load a saved game
        12: extra,  # display extra options
        18: quit_game  # quit the game
    }

    while True:
        Functions.clear_screen()
        draw("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        draw("lang/PL/menu_glowne_instrukcje.txt")

        # draw menu items from start_position to end_position
        rysuj_oddo("lang/PL/menu_glowne.txt", start_position, end_position)

        keyboard_key = Functions.getkey()

        # move cursor up
        if keyboard_key == 'w' and start_position >= 6:
            start_position -= 6
            end_position -= 6
        # move cursor down
        elif keyboard_key == 's' and start_position >= 0 and end_position < 23:
            start_position += 6
            end_position += 6
        # quit game
        elif keyboard_key == 'esc':
            quit_game()
        # execute selected menu option
        elif keyboard_key == 'return':
            # calculate the index of the selected option
            selected_option = start_position // 6 * 6
            # get the corresponding function and execute it
            menu_options.get(selected_option, quit_game)()


def start_new_game(level=None, map_size=None, life_points=None, strength=None):
    """Starts a new game with the specified parameters or the default ones if none are given."""
    player = Members.Player()

    # prompt the user to enter a name for the player
    while player.name == '':
        try:
            player.name = input("\n\tENTER HERO NAME\n\t")
            if len(player.name) > 9:
                raise ValueError('Name is too long. Maximum 9 characters allowed.')
        except ValueError as e:
            print(e)
            player.name = ''

    Functions.status = ''

    if level is not None or map_size is not None or life_points is not None:
        # if custom parameters are provided, use them
        Undergrounds.poziom_p = level.get()
        game_map = mapsgen
        player.life_points = life_points.get()
        player.s = strength.get()
    else:
        # otherwise, use default parameters
        Undergrounds.poziom_p = 1
        game_map = Undergrounds.Mapa()
        game_map.przygotuj_mape()

    game_map.mapa[0][0] = player
    player.take_position(game_map)
    Functions.widocznosc(player, game_map)
    game_map.rysuj_mape()
    Functions.poruszanie_po_mapie(player, game_map)

    
def load_game():
    """Loads a saved game from a file.

    Reads a pickled file and extracts the player, map, level, items, and tasks from it. Then prompts the user for a hero
    name if one is not already set, places the player on the map, draws the map, and moves the player around until the
    game is closed or won."""
    # Check if save file exists
    if (os.path.exists(PIK)):
        # Load data from file
        data2 = []
        gr = Members.Player()
        maps = Undergrounds.Mapa()
        with open(PIK, "rb") as f:
            for _ in range(pickle.load(f)):
                data2.append(pickle.load(f))
                gr = data2[0]
                maps = data2[1]
                Undergrounds.poziom_p = data2[2]
                gr.list_of_item = data2[3]
                gr.tasks = data2[4]

                # Prompt user for hero name if not already set
                if gr.name == '':
                    gr.name = input("ENTER HERO NAME\n\t")

                # Place player on map and draw it
                gr.take_position(maps)
                maps.rysuj_mape()

                # Move player around the map
                Functions.poruszanie_po_mapie(gr, maps)
    else:
        # Display error message if save file does not exist
        Functions.clear_screen()
        draw("static/error_msg/load_save_error")
        Functions.get_char(False)
        return


def quit_game():
    """Exits the game.

    Exits the game with a return code of 0."""
    sys.exit(0)

    
def extra():
    """Displays the "Extra" menu and handles user input."""
    start_position = 24
    end_position = 28

    # menu options with their corresponding functions
    menu_options = {
        24: generator,
        29: opcje,
    }

    while True:
        Functions.clear_screen()  # clear the screen
        draw("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        draw("lang/PL/menu_glowne_instrukcje.txt")
        rysuj_oddo("lang/PL/menu_glowne.txt", start_position, end_position)

        keyboard_key = Functions.getkey()
        # move cursor up
        if keyboard_key == 'w' and start_position >= 28:
            start_position -= 5
            end_position -= 5
        # move cursor down
        elif keyboard_key == 's' and start_position >= 24 and end_position < 37:
            start_position += 5
            end_position += 5
        # quit menu
        elif keyboard_key == 'esc':
            return
        # execute selected menu option
        elif keyboard_key == 'return':
            selected_option = start_position
            if selected_option == 34:
                return
            menu_options.get(selected_option)()
                
def opcje():
    od = 39
    do = 43  
      
    while True:
        Functions.clear_screen()  # czyszczenie ekranu
        draw("static/LOGO.txt")
        print(f"\t Version: {Version.GAME.value}")
        print(f"\t Python : {platform.python_version()}")
        draw("lang/PL/menu_glowne_instrukcje.txt")
        rysuj_oddo("lang/PL/menu_glowne.txt",od,do)
        keyboard_key = Functions.getkey()
        if keyboard_key == 'w' and od >= 43:
            od -= 5
            do -= 5
        elif keyboard_key == 's' and od >= 39 and do < 52:
            od += 5
            do += 5
        elif keyboard_key == 'esc':
            return
        elif keyboard_key == 'return':
            if od >=39 and do <=43:
                Functions.get_char()
            elif od >=43 and do <=48:
                Functions.clear_screen()  # czyszczenie ekranu
                draw("static/O_GRZE.txt")
                Functions.get_char() 
            elif od >=48 and do <=54:
                return
    
if __name__ == "__main__":
    main_menu()
