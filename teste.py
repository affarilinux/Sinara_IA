'''import keyboard
import sys
from time import sleep

def kb():
    while True:

        if keyboard.is_pressed("ctrl+a"):
            print("A key was pressed")
            sys.exit()
        keyboard.add_hotkey("esc",at)
        
        
def at():
    quit()

def main():

    kb()

if __name__ == "__main__":

    main()'''

'''import keyboard

def mywait():
    keyboard.read_key()

def my_function():
    print("hello")

def my_exit():
    quit()

keyboard.add_hotkey('h', my_function)
keyboard.add_hotkey('esc', my_exit)

while True:
    mywait()'''

#import keyboard

'''def at():
    print(4566)
    quit()
# press a to print rk
ass = True
while ass:
    keyboard.add_hotkey('a', lambda: quit())
    ia = input("ai sim:")

    if ia == "s":
        ass = False'''

#keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey'))
  
#keyboard.wait('esc')

import keyboard
import sys
from time import sleep

def kb():
    #while True:

        # keyboard.is_pressed("ctrl+a"):
    keyboard.is_pressed("ctrl+a")
            #print("A key was pressed")

            #sys.exit()
            #quit()
            

        
    

def main():

    kb()

if __name__ == "__main__":

    main()