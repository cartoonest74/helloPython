import os
from time import sleep

def clear():
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')