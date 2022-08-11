# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:28:32 2021

@author: ninad
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:02:36 2021

@author: ninad
"""

import Rotors
wiring=Rotors.Rotor()
RotorSettingopz=[]
def runThrough(Rotor_num,inputy,Rotor_settingy):
    inputy = (inputy+Rotor_settingy) % 127;
    return wiring[Rotor_num][inputy];
def plug(plugboard,key):
    if plugboard[key]==(-1):
        return key
    else:
        return plugboard[key]
reflector=[127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
def encrypt(Rotor_combinationz,RotorSettingz,plugboardz,x):
    x=plug(plugboardz,x)
    connectTo=x
    s=x
    
    #ciphering block
    for i in range(0,300):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    s=reflector[s]
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    triger=1
    counter=0
    connectTo=plug(plugboardz,connectTo)
    #incrementing the 1st rotor setting by 1     
    while triger==1:
        RotorSettingz[counter]+=1
        if RotorSettingz[counter]>127:
            RotorSettingz[counter]=0
        else:
            triger=0
        counter+=1
        RotorSettingopz=RotorSettingz
        RotorSettingz=[]
    return Rotor_combinationz,RotorSettingopz,connectTo
def decrypt(Rotor_combinationz,RotorSettingz,plugboardz,x):
    x=plug(plugboardz,x)
    connectTo=x
    s=x
    
    #ciphering block
    s=reflector[s]
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    s=reflector[s]
    
    for i in range(0,300):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    triger=1
    counter=0
    connectTo=plug(plugboardz,connectTo)
    #incrementing the 1st rotor setting by 1     
    while triger==1:
        RotorSettingz[counter]+=1
        if RotorSettingz[counter]>127:
            RotorSettingz[counter]=0
        else:
            triger=0
        counter+=1
        RotorSettingopz=RotorSettingz
        RotorSettingz=[]
    return Rotor_combinationz,RotorSettingopz,connectTo
