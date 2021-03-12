import numpy as np
import random
import matplotlib.pyplot as plt

a=[];
b=[];

z=0;
x=0;

for i in range(1,1000):
    prize = ['goat', 'goat', 'car']
        
    # seleccion de puerta invitado
    choice1 = random.randint(0,2); 
    
    if prize[choice1] == "car":
        z+=1
    a.append(z);
    
    #seleccion de la puerta host
    choice2 = random.randint(0,2); 
    if prize[choice2] == "car":
        x+=1
    b.append(x);   
    
    #opcion  de otra puerta
    choice1 = random.randint(0,2); 
    if prize[choice1] == "car":
        z+=1
    a.append(z); 


plt.plot(a)
plt.plot(b)
plt.show()