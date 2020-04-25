# Faça um programa que abra e reproduza um áudio de arquivo mp3
from pygame import mixer
mixer.init()
mixer.music.load('moonlight.mp3')
mixer.music.play()
x = input('Digite algo para parar...')


