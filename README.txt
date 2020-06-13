A quick keyboard script because I got tired of not being able to save playlists for Discord bots.

1) Install https://github.com/boppreh/keyboard and put "script.py" into keyboard-master.

2) Create a folder "playlists" in keyboard-master containing txt files with song identifiers separated with new lines, i.e. "chillTunes.txt" contains:
song 1 artist 1
song 2 artist 2
song 3 artist 3

3) Create "settings.txt" in keyboard-master with three lines indicating the Discord bot, playlist name, and loop (yes/no), i.e.:
Groovy
chillTunes
yes

4) Run "script.py". Focus the Discord message bar and hit 'esc'. Wait for script to finish running.