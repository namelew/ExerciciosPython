import pygame
# Iniciando o mixer
pygame.mixer.init()
# Iniciando o pygame
pygame.init()
pygame.mixer.music.load('Arquivo MP3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
