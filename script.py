#Installs

import keyboard
import time

#Settings

settings_file = open("settings.txt", "r")
settings = settings_file.read().split('\n')

player = settings[0] #CHOICE 1: Discord Bot

if (player == "Groovy"):
    prefix = "-"
if (player == "Rythm"):
    prefix = "_"

selection = settings[1] #CHOICE 2: Playlist Name
loop = settings[2] #CHOICE 3: Loop (yes/no)

#Import playlists

playlist = open("playlists/" + selection + ".txt", "r")
songs = playlist.read().split('\n')

#Keyboard shortcuts

keyboard.wait("esc")
for x in songs:
    keyboard.write(prefix + "play " + x + "\n")
    time.sleep(3)
if (loop == "yes"):
    keyboard.write(prefix + "loop" + "\n")