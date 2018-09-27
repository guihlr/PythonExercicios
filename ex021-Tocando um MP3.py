# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.mixer.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# Posso usar tambem

import playsound

playsound.playsound('ex021.mp3')
