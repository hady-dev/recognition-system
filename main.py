import face_dataset
import face_recognition
import face_training

import cv2
import json
from pynput import keyboard
import time
import os

def Read_data():
    global names
    with open('dataset/data.JSON', 'r') as f:
        names = json.loads(f.read())
    global ids
    ids = []
    i = 0
    for each in names:
        ids.append(i)
        i += 1

def add_user():
    global name
    NameNotEntered = True
    while NameNotEntered:
        name = input("Enter new user's name then Press 'Enter' : ")
        name = name[1:]
        input1 = input("Just To Confirm, Press 'y' if The Name is '" + str(name) + "' else Press 'n' then press 'Enter'")
        if input1 == "y":
            NameNotEntered = False
                
    face_dataset.Start(len(ids))
    names.append(name)
    with open('dataset/data.JSON', 'w') as f:
        f.write(json.dumps(names))
    face_training.Start()

def Start_Recognition():
    Read_data()
    face_recognition.Start(names)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    Read_data()
    print("There is " +  str(len(ids) - 1)  + " Users")
    #choice = input("Enter the Index Next to Your Choice : \n1 - Add User \n2 - Start The Software\n")
    print("Enter the Index Next to Your Choice : \n1 - Add User \n2 - Start The Software\nq - Quit\n")
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('1'):
            choice = 1
        elif event.key == keyboard.KeyCode.from_char('2'):
            choice = 2
        elif event.key == keyboard.KeyCode.from_char('q'):
            choice = "q"
        else:
            choice = 21321
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == 1:
        add_user()
        Read_data()
        print("There is " +  str(len(ids) - 1)  + " Users")
    elif choice == 2:
        Start_Recognition()
    elif choice == "q":
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()
    else:
        print("Please Enter a valid choice")
    
