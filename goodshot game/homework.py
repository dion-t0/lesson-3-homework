import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="GoodShot game"

gun=Actor("gun")
gun.pos=50,50
message='click on gun otherwise u die!'


def draw() :
    screen.fill("black")
    gun.draw()
    screen.draw.text(message,center=(200,20), fontsize=30, color="white")

def move_gun() :
    gun.x=random.randint(50,450)
    gun.y=random.randint(50,450)

def on_mouse_down(pos):
    global message 
    
    print("watch out for bulllets!")

    
    if gun.collidepoint(pos):
        message="u stopped the gun"
        move_gun()
    else:
        message="u got hit with the gun!"



move_gun()

pgzrun.go()