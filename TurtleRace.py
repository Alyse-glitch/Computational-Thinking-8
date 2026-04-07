from utils import *
# note from Josh: your ducks are starting in weird places. Make sure you fix those 
# starting points by changing stuff in SECTION 1
# once their starts look good, uncomment the lines in section 3 to make them race 
# (lines 34 - 45)
# use CTRL /
print("Which duck do you think is going to win? A Pink Duck, B Blue Duck, C Black Duck, or D Yellow Duck")
input("")
print(f"Well good luck to your duck, and may your odds ever be in your favor!")
# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 195
x2 = -300
y2 = 80
x3 = -300
y3 = -55
x4 = -300
y4 = -200



# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("Pond")
t1 = create_sprite("pink",x1,y1)
t2 = create_sprite("Blue duck",x2,y2)
t3 = create_sprite("Black Duck",x3,y3)
t4 = create_sprite("yellow duck",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(40):
    x1 += 6
    x2 += random.randint(5,15)
    x3 += 15
    x4 += 10

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("Bread",-200,-200)
if x3 >= x2 and x3 >= x1 and x3 >= x4:
    s5.write("Black Duck wins!")
elif x2 >= x1 and x2 >= x3 and x4 >= x4:
    s5.write("Blue Duck wins!")
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Pink Duck wins!")
elif x4 >= x2 and x4 >= x1 and x4 >= x3:
    s5.write("Yellow Duck wins!")

turtle.exitonclick()