""" 
This is the module that includes a function 
with which you can generate three random 
numbers between 0 and 1. it will return these 
three numbers within a tuple 
 
"""

import time
import random

def generator():
    time.sleep(.1)
    a = random.random()
    b = random.random()
    c = random.random()

    return (a,b,c)

if __name__ == "__main__":
    for i in range(10):
        result = generator()
        print(result)


