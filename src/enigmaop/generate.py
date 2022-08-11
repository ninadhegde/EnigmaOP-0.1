# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:47:05 2021

@author: ninad
"""
import random
def random_settings():
    RotorSettingx=[]
    Rotor_combinationx=[]
    lstx=[] 
    for i in range(0,350):
        lstx.append(i)
        #Taking a random setting all rotors set to zero
    for i in range(0,300):
        RotorSettingx.append(random.randint(0, 127))
        s=random.choice(lstx)
        Rotor_combinationx.append(s)
        lstx.remove(s)
    lst2x=[0]*128    
    lst2x=random.sample(range(0, 128), 120)
    plugboardx={}
    for i in range(0,119,2):
        key=lst2x[i+1]
        value=lst2x[i]
        plugboardx[key]=value
        plugboardx[value]=key
    return Rotor_combinationx , RotorSettingx , plugboardx
