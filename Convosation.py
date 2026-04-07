# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("moon")

s1 = create_sprite("Mickey Mouse", -200, 0)
s2 = create_sprite("Remy", 200, 0)
s3 = create_sprite("Robby",0,0 )

s1.color("Yellow")
s2.color("dark red")
s3.color("White")
time.sleep(5)

s1.write("Hi nice to meet you.",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("Nice to meet you!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s3.write(f"I'm looking for my aunt{player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.clear()
s3.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.clear()
s2.write(f"I'm also looking for my aunt {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
s1.write("I just saw them at the cheese festival! ",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s3.write("Lets all go to the cheese festival to look for her!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

set_background("cheese festival")



######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()