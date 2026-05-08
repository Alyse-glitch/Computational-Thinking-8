
#The goal of my game is If you get number amount of watermelons then you get one hippo and each time the cost goes up 

from utils import *

# Section 1 - setup
set_background("Hippo Water")

Watermelon = 0
BabyHippo = 0
Cost = 10

def get_Watermelon():
    global Watermelon
    Watermelon += 1
    x = random.randint(-200,200)
    y = random.randint (-200,200)
    create_sprite("Watermelon",x,y)
window.onkeypress(get_Watermelon, "w")
# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()

def get_BabyHippo():
    global BabyHippo, Cost, Watermelon
    if Watermelon >= Cost:
        Cost = 2*Cost
        BabyHippo += 1
        x = random.randint(-200,200)
        y = random.randint (-200,200)
        create_sprite("BabyHippo",x,y)
window.onkeypress(get_BabyHippo, "b")
# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(100):
    m1.clear()
    m1.write(f"Watermelon):{Watermelon}\nCost: {Cost}\nBabyHippo: {BabyHippo}", font=("Arial",30, "normal"))    
    Watermelon += BabyHippo
    time.sleep(0.01)
    window.update()