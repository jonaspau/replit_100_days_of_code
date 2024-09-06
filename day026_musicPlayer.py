import os
import time
import pygame


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('day026_audio.wav')

def pause():
  pygame.mixer.pause()

def play():
  # Play the sound
  sound.play()
  while True:
    stopPlaying = int(
      input("Press 2 anytime to stop the music and go back to the menu: ")
    )
    if stopPlaying == 2:
      pause()
      return
    else:
      continue

while True:
  # clear the screen 
  os.system('clear')
  # Show the menu
  print("--- myTunes ---")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  # take user's input
  userInput = int(input("Choice: "))
  # check whether you should call the play() subroutine depending on user's input
  if userInput == 1:
    print("Playing ...")
    play()
  elif userInput == 2:
    print("Exiting")
    exit()
  else:
    continue