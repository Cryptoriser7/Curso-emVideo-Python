#Faça um programa em python que abra e reproduza o audio de um arquivo .mp3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#'''Solução do video nao funcionou. Outra solução abaixo.'''

#import playsound
#playsound.playsound('ex021.mp3')

