from pygame import mixer
from datetime import datetime
from time import time

def music(file,stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stop:
            mixer.music.stop()
            break
def log_now(msg):
    with open("Historylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':

    init_water = time()
    init_exercise = time()
    exerc = 2*60*60
    water = 30*60

    while True:
        if time() - init_water > water:
            print("Paani Peele time ho gaya...\n Enter 's' to stop the alarm.")
            music('water.mp3', 's')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_exercise > exerc:
            print("Exercise ka time ho gaya...\n Enter 'p' to stop the alarm.")
            music('workout.mp3', 'p')
            init_exercise = time()
            log_now("physical exercise at")

