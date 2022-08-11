
import Rotors
reflector=[127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

wiring=Rotors.Rotor()
RotorSettingopz=[]

def get_key(wire_dict,val):
    '''
    for key, value in x.items():
         if val == value:
             return key
    '''
    key_list = list(wire_dict.keys())
    val_list = list(wire_dict.values())
    position=val_list.index(val)
    return key_list[position]
         

def runThrough(Rotor_num,inputy,Rotor_settingy,forward):
    
    
    if forward: 
        inputy = (inputy+Rotor_settingy) % 127
        #print('inside runthrough :\tinput = '+str(inputy))
        return wiring[Rotor_num][inputy];
    else:
        '''
        #inputx = (inputy+Rotor_settingy) % 127
        print('inside runthrough :\trev input = '+str(inputy))
        return (get_key(wiring[Rotor_num],inputy)+Rotor_settingy)%127
        '''
        for i in range(0,128):
            if inputy== wiring[Rotor_num][i]:
                output=i-Rotor_settingy
                while output<0:
                    output=127+output
                output=output%127
                return output
              

def plug(plugboard,key):
    try:
        return plugboard[key]
    except KeyError:
        
        return key
        


def encrypt(Rotor_combinationz,RotorSettingz,plugboardz,x,level):
    
    #forward plugboard
    x=plug(plugboardz,x)
    
    connectTo=x
    s=x
    print('after plugging = '+str(x))
    
    #Forward block
    for i in range(0,level):
        
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i],True)
        connectTo=s
        print('after roter : '+str(Rotor_combinationz[i])+' = '+str(s))
    
   
        
    #Reflector
    s=reflector[s]
    print('after reflector :  = '+str(s))
    
    #Reverse Block
    for i in range(level-1,-1,-1):
        
        
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i],False)
        
        print('after roterRevr : '+str(Rotor_combinationz[i])+' = '+str(s))
    
    connectTo=s
    
    #Reverse plugboard
    connectTo=plug(plugboardz,connectTo)
    print('after plugging = '+str(connectTo))
    
    triger=1
    counter=0
    
    #incrementing the 1st rotor setting by 1     
    while triger==1 and counter<level:
        
        
        RotorSettingz[counter]+=1
        if RotorSettingz[counter]>127:
            for i in range(len(RotorSettingz)):
                if RotorSettingz[i] == 0:
                    i=counter
                    
                    RotorSettingz[i]= 0
        else:
            triger=0
        counter+=1
        RotorSettingopz=RotorSettingz
    
    return Rotor_combinationz,RotorSettingz,connectTo
'''
def decrypt(Rotor_combination,RotorSetting,plugboard,x):
    
    #forward plugboard
    x=plug(plugboard,x)
    
    
    s=x
    print('after plugging = '+str(x))
    
     #Forward block
    for i in range(0,5):
        
        s=runThrough(Rotor_combination[i],s,RotorSetting[i],True)
        connectTo=s
        print('after roter : '+str(Rotor_combination[i])+' = '+str(s))
    
        
    
    #Reflector
    s=reflector[s]
    print('after reflector :  = '+str(s))
    
    
    #Reverse Block
    for i in range(4,-1,-1):
        
        s=runThrough(Rotor_combination[i],s,RotorSetting[i],False)
        connectTo=s
        print('after roterRevr : '+str(Rotor_combination[i])+' = '+str(s))
    
    
    #Reverse plugboard
    connectTo=plug(plugboard,connectTo)
    print('after plugging = '+str(connectTo))
    
    triger=1
    counter=0
    #print('base setting'+ str(RotorSetting))
    #incrementing the 1st rotor setting by 1  
    
    while triger==1 and counter<300:
        #print(RotorSetting)
        RotorSetting[counter]+=1
        if RotorSetting[counter]>127:
            RotorSetting[counter]=0
            #print('inside while if'+ str(RotorSetting))
        else:
            triger=0
            #print('inside while else'+str(RotorSetting))
        counter+=1
        RotorSettingop=RotorSetting
        
        #print('before return'+str(RotorSetting))
    
    return Rotor_combination,RotorSetting,connectTo

'''