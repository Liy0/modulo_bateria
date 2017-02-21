#!/usr/bin/env python

"""openbate.py: Trigger script para baterias electricas."""

__author__ = "Pablo Perez"
__email__ = "pablomartin.it@gmail.com"

import pygame
import readchar

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

class Modulo:

    def __init__(self):
       self.SOUND_MAPPING = {
            0: 'kick.wav',
            1: 'snare.wav',
            2: 'open.wav',
            3: 'closed.wav',
            4: 'clap.wav',
            5: 'cymbal.wav'
       }
       self.cuerpos = [0,0,0,0,0,0]

    def kit(self,kit):
        for key, soundfile in self.SOUND_MAPPING.iteritems():
            self.cuerpos[key] = pygame.mixer.Sound(kit+"/"+soundfile)
            self.cuerpos[key].set_volume(0.1);

    def mas_volumen(self):

        v = self.cuerpos[0].get_volume() + (self.cuerpos[0].get_volume() * 0.30)
        #print v
        v_int = int(round(v*100))
        if v_int > 100:
            v = 100
        if v_int == 0:
            v = 1
        #print v_int
        for c in self.cuerpos:
            c.set_volume( v );

    def menos_volumen(self):
        v = self.cuerpos[0].get_volume() - (self.cuerpos[0].get_volume() * 0.30)
        v_int = int(round(v*100))

        if v_int < 0:
            v_int = 0

        #print v_int

        for c in self.cuerpos:
            c.set_volume( v_int );

m = Modulo();
m.kit("samples")

while True:
    c = readchar.readchar()    

    if (ord(c) == 44):
        print "\t\t\t\t\t\t\t\t\t\t\t"+c
        m.menos_volumen()
        continue

    if (ord(c) == 46):
        print "\t\t\t\t\t\t\t\t\t\t\t\t"+c
        m.mas_volumen()
        continue

    if (ord(c) == 97):  # A
        print "\t"+c
        m.cuerpos[0].play()

    if (ord(c) == 115):  # S
        print "\t\t"+c
        m.cuerpos[1].play()

    if (ord(c) == 100):  # D
        print "\t\t\t"+c
        m.cuerpos[2].play()

    if (ord(c) == 106):  # J
        print "\t\t\t\t\t"+c
        m.cuerpos[3].play()

    if (ord(c) == 107):  # K
        print "\t\t\t\t\t\t"+c
        m.cuerpos[4].play()

    if (ord(c) == 108):  # L
        print "\t\t\t\t\t\t\t"+c
        m.cuerpos[5].play()

    if (ord(c) == 3):
        print "Chaucha..."
        break

