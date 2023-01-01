'''
Play a song from this repl and build a menu to go with it. Make it look like an iPod!
~Use a while true loop to create a title for a music player.
~Allow the user to select to play a song and use subroutine called 'play' when they select the song.
~Give the user the option to exit the program.
~The title should pop up and pause along with the menu options.
~If the user chooses anything else, start again by clearing the screen.
'''

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue

