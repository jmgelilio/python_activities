import time
import os


def Hi():
    print("Hi! This is JM. I will close it in")
    for x in range(5,0,-1):
        print(x)
        time.sleep(1)
    time.sleep(0.5)
    print("BYE BYE!")
    time.sleep(1)
    os.system('cls||clear')
    
Hi()