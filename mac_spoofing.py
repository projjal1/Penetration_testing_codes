#Code to generate new mac address (spoofing MAC)
#will work on Linux envs(Parrot OS preferrably)

import random
import os
import subprocess 

#Random function generator
def get_rand():
    return random.choice("abcdef0123456789") 

#Function to generate new MAC address
def new_mac():
    new_ = "" 
    for i in range(0,5):
        new_ += get_rand() + get_rand() + ":"  
    new_ += get_rand() + get_rand() 
    return new_

#Command to fetch current mac address
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

#disable current mac for the system
subprocess.call(["sudo","ifconfig","eth0","down"])

#get new mac
new_m = new_mac() 

#assign new mac address
subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m]) 

#enable interface with new mac address
subprocess.call(["sudo","ifconfig","eth0","up"])

#print the current mac address
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))
