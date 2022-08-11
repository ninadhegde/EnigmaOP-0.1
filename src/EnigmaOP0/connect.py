# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:00:29 2021

@author: ninad
"""
import Rotors
wiring=Rotors.Rotor()
def runThrough(Rotor_num,inputy,Rotor_settingy):
    inputy = (inputy+Rotor_settingy) % 127;
    return wiring[Rotor_num][inputy];
def plug(plugboarda,key):
    if plugboarda[key]==(-1):
        return key
    else:
        return plugboarda[key]