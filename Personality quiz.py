name=input("Welcome to my quiz! What is your name?")
input("")
print(f"Hello {name}, ready to start my quiz?")
input("")
Spicy_points=0
Sweet_points=0
Basic_points=0

answer1=input("What is your favorite food?  A Buldak noodles, B Ice Cream, or C Potato chips?")
if answer1 == "A" or answer1 == "a":
    Spicy_points += 1
elif answer1 == "B" or answer1 == "b":
    Sweet_points += 1
elif answer1 == "C" or answer1 == "c":
    Basic_points += 1

answer2 = input("What is your go to candy? A M&Ms, B Skittles, or C HotTamales?")

if answer2 == "A" or answer2 == "a":
    Basic_points += 1
elif answer2 == "B" or answer2 == "b":
    Sweet_points += 1
elif answer2 == "C" or answer2 == "c":
    Spicy_points += 1

answer3 = input("Would you rather eat A Mango, B Apple, or C Chile Pepper?")

if answer3 == "B" or answer3 == "b":
    Basic_points += 1
elif answer3 == "A" or answer3 == "a":
    Sweet_points += 1
elif answer3 == "C" or answer3 == "c":
    Spicy_points += 1 

answer4 = input("What would you dip your chips in? A Salas, B Ketchup, or C Sweet and sour sauce?")

if answer4 == "B" or answer4 == "b":
    Basic_points += 1
elif answer4 == "C" or answer4 == "c":
    Sweet_points += 1
elif answer4 == "A" or answer4 == "a":
    Spicy_points += 1 

    answer5 = input("What type of chicken do you prefer? A Orange chicken, B Spicy chicken , or C Plain chicken?")

if answer4 == "C" or answer5 == "c":
    Basic_points += 1
elif answer4 == "A" or answer5 == "a":
    Sweet_points += 1
elif answer4 == "B" or answer5 == "b":
    Spicy_points += 1 

# End: three different types of points
if Spicy_points > Sweet_points and Spicy_points > Basic_points:
    print("You really like spicy foods! I can't even eat Takis without my mouth burning!")
elif Sweet_points > Spicy_points and Sweet_points > Basic_points:
    print("You really like sweets! Did you know Zendaya loves coffee ice cream?")
elif Basic_points > Spicy_points and Basic_points > Sweet_points:
    print("You're a pretty basic person! But I think you should try some thing for a change!")