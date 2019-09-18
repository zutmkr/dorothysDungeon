
![Logo](https://github.com/zutmkr/Studia/blob/master/praca_inz/static/logo.PNG)

NOTE! This code is final... development has moved [here.](https://github.com/zutmkr/Studia/tree/master/praca_mag "Dorothy's Dungeon 2")














## (Beta v0.2.1.190918):
### [CODE REFACTOR]:
        + initial commit

## (Beta v0.2.1.180308):
### [CODE + HOTFIX]:
        + fixed a bug that prevented the game from running (missing file)
        + fixed some of the texts in the game
        + improved methods responsible for drawing images
        + a new Gargoyle appearance

# (Beta v0.2):
### [CODE]:
        + corrected file encoding (\ EN \ menu_enabled_test.txt)
        + added instructions to close the file in the drawujobrazy module
        + light code ordering
### [NEW FEATURE]:
        + unlocked option ABOUT GAME

# (Beta v0.1b):
### [EDITOR v0.03]:
        + the LOAD window has been improved
        + minor errors fixed
### [NEW FEATURE]:
        + added information about the status of the current task

# (Beta v0.1a):
### [NEW FEATURE]:
        + underground editor v0.02
        + added a second task for the Merchant

# (Beta v0.020RC):
### [CODE]:
        + adding the A * search algorithm
        + map is generated in three variants of size
### [KNOWN BUGS]:
        + selecting the 'new game' on the death screen takes you to the Main menu
         ++ fixed (python turned out to use '__main__ import' to use initializer script methods)

# (Alpha v0.013):
### [CODE]:
        + error caught by the exception is now saved to the file
### [NEW FEATURE]:
        + tasks and rewards for the player
         ++ info (Only 1 trader's job)
        + table with the number of points collected at the end of the game
        + the ability to name your character
### [KNOWN BUGS]:
        + the scoreboard does not write to the screen after the player's death

# (Alpha v0.012):
### [QUALITY OF LIFE]:
        + added version number of the game at LOGO
        + added ability to go back to the game on the game over screen
        + the player will know faster if he sells / buys
        + improved formatting of item names on the trade screen
         ++ fixed (legends are badly displayed)
        + legend obtained on the map (status) is now described more concretely
### [CODE]:
        + the battle balance has been modified
        + improved GAME OVER screen
        + specify item stats
        + optimize the Player.handel () method
        + healer scales with the dungeon level
        + damage dealt by monsters scales with the level of the dungeon
        + fixed the reset of the dungeon level after the player has begun a new game from the game over screen
        + blacksmith and tradesman tag removed from the map view
         ++ hotfix (I also accidentally removed info about the backpack and the form ..)
        + add statistics to items
         ++ fixed (problem with assigning string +5 to non-legendary items, items from sale are copying to the backpack at the exit from the trader)

# (Alpha v0.011):
        + main game menu
        + prize (gold) for wins won
        + save game option
        + support for coding Polish characters
        + increased damage dealt by the player to 15 on the 1st level
        + increased chances of escaping to 25%
        + trading was programmed
        + healer scales with the level
        + gold number indicator added to the character screen

# (Alpha v0.010c):
        + added the ability to buy items from the trader and a smooth selection of items from the list
        + added the possibility of meeting a trader and basic interaction with him

# (Alpha v0.010b):
        + added the possibility of starting a new game on the 'game over' screen
        + the player only receives one item per room

# (Alpha v0.010a):
        + three new opponents added
        + description and blacksmith sign added to the player's interface (no upgrading of items yet)
        + added level descent marker in the underground
        + added description and trader's mark to the player's interface (no trading has been programmed yet)
        + fixed a bug using the exit button from the game

# (Alpha v0.010):
        + refactoring of the code
        + added the sound of getting the legendary item
        + changed the sound of the player's attack and the death of the opponent to a more pleasant one for the ear

# (Alpha v0.09d):
        + change of map drawing algorithm. The map is drawn only when the player discovers the fields

# (Alpha v0.09c):
        + fighting sounds added
        + fixed map discovery at 2+ levels

# (Alpha v0.09b):
        + added dynamic map discovery

# (Alpha v0.09a):
        + death animations of the player added

# (Alpha v0.09):
        + improved display of monster life values ​​(maxPZ)
        + added scaling of the monster's life depending on the level of the dungeon
        + combat escape options have been programmed (20% chance)
        + you can leave the game with the "`" sign in the 'map' view

# (Alpha v0.08):
         + the game ends only with the death of the player (infinite dyngeons, yay!)
         + added 'status bar' telling what's going on with the character
         + battle mode added
         + show_states -> show the character card
         + events in all directions
         + a lot of changes in quality of life
         + when a player finds a legendary item that will permanently give him +5 strength
         + and a lot of other things that I do not remember ...

# (Alpha v0.03):
         + a line was added asking where the player should go
         + increased time of displaying information for the player to 1 second (from 0.3s)

# (Alpha v0.02):
         + added support for moving the player without the need to accept the action using the 'enter' key
         + added the sleep () method from the 'time' library so that the screen does not clear too quickly by erasing the player's feedback instructions

# (Alpha v0.01):
         + the first playable version
