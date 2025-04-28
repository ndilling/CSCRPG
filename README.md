# CSCRPG
CSC 102 Project

CSCRPG is a turn based role playing game created using Python and Pygame. In this game, the player chooses a character class, assigns stat points to build their character, and battles through a series of enemies leading up to a final boss. The game includes several features such as unique abilities for each class, a system where players and enemies take turns attacking, spells that have cooldown periods, status effects like burning, bleeding, and stunning, a live combat log that describes the action, and a save and load system that allows players to continue their progress later.

The structure of the project is organized into several different files, each with a specific role. The file named main.py acts as the main launcher for the game. It controls the flow of the game, starting from the title screen, moving into character creation, and continuing through the battles. It is also responsible for saving and loading the player’s progress. The constants.py file holds important values that are used throughout the game, such as screen dimensions, color codes, experience point rules, font sizes, and layout settings. By keeping these values in one place, the game remains consistent and easy to adjust if needed.

The data.py file is where all the game’s abilities and enemies are defined. It separates abilities according to character class, and it also lists the enemies and boss characters, giving them names, health points, and available moves. It includes a list of player stats called STAT_NAMES, which are used during the stat allocation process when the player builds their character.

The characters.py file defines how the Player and Enemy characters behave. The Player class manages things like stat upgrades, leveling up after battles, and keeping track of the character’s abilities and experience points. The Enemy class is used to create opponents for the player to fight, pulling information from the data.py file.

The screens.py file controls everything that the player sees and interacts with. It includes the title screen, the class selection screen, the stat allocation screen, the combat screen, and the victory or defeat screens. It also handles combat turns, spell cooldowns, the display of health bars, and the live combat log that tells the player what is happening during each fight.

The gui_utils.py file contains helpful drawing functions. These functions are used to display text, draw health bars, show tooltips when the player hovers over something, and manage the appearance of the live combat log. These tools help keep the game’s visual design clean and organized.

The tooltips.py file provides short descriptions for the player’s stats and classes. These descriptions are shown as tooltips when the player hovers the mouse over different options during character creation or combat.

Finally, the save_data.json file is created while the game is running. It stores the player’s name, class, stats, level, experience points, and the number of battles they have completed. This allows players to leave and return to the game without losing their progress.

All of these files work closely together to create a smooth and complete gaming experience. The main.py file controls the overall flow of the game. It relies on screens.py to display each part of the game and to interact with the player. Screens.py uses characters.py to create and manage the player and enemy characters. It pulls information from data.py to know which abilities and enemies exist. Gui_utils.py makes it easy to draw important elements like health bars and text, while tooltips.py provides helpful descriptions when needed. Constants.py keeps everything looking consistent, and save_data.json ensures that the player’s progress is not lost. Together, these files create a turn based RPG that is easy to understand and flexible enough to expand with new abilities, characters, or features in the future.

main.py code/program is the main program you will be running. Every other file is loaded or brought into this main.py file to be used accordingly. Such as the character creation modules and the screens.

We suggest running this game on a personal computer as opposed to a school computer.

Make sure pygame, json, matplotlib, and OS are installed on your personal computer / imported. Make sure to install and run your file from the Terminal.

Hit "n" for a new game / to start game. Choose any of the 5 options that are presented.

Stats overview: You may choose whatever stats you want Fighter: focus on strength and constitution Paladin: focus on strength and constitution Sorcerer: focus on intelligence and constitution Cleric: focus on strength and constitution Ranger: focus on strength and constitution #You may choose whatever you want these are just tips to make game more balanced Use all 20 points then hit confirm when ready

You have two options for abilities Sometimes there will be a countdown for when you use an ability. This is a cooldown timer, it will countdown based on terms. (Can't use the move for a certain period of time) Go through hitting abilities till you win. There are many options but this is for the user to pick and have fun with. Play around however you want, some classes have healing abilities and such. Every class has different spells or abilities and you should try each one as they offer a very different experience.

There is hover over on all abilities by running the cursor over the ability name. This will tell you what they do and the effects they have.

Good luck adventurer!

Examples of output:

https://docs.google.com/document/d/1cAdGVrY4ozzAihFn2w0w0ZQAkhcq6Qr-/edit?usp=sharing&ouid=107196544892090442781&rtpof=true&sd=true
