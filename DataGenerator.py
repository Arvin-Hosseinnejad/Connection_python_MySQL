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


