#Project Treasure Island
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#Part of the Udemy 100 Days of Python--Day 3 Project

print("Welcome to Treasure Island.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Your mission is to find the treasure. Enter your response from the *starred* choices provided within the prompts.") 

first_choice = input("You found a note with a minimalistic map to the treasure hidden under a rock. One side of the map is green with sqiggles. The other side of the map displays a small yellow circle on a background of blue. The yellow circle has a large red 'X' inside a box (a building of some sort?). You look down and see a large lake downhill, seen beyond the forest treetops - this must be the blue side of marked on the map! But to get there...you have to go down the hill and through the forest in the dark. Will you take the  *left*  or  *right*  path into the dark forest?   ")
print(first_choice)
first_choice = first_choice.lower() 

if (first_choice == "left"):
    second_choice = input("You made it to the lakeshore with only a few scrapes, bug bites, and maybe touch of poisen ivy. Or is that a spider? It's as quiet as the grave by the riverside; the water surface remains unbroken in the moonlight. Is that a building on a small island in the middle of the lake? Will you  *swim*  across the suspiciously calm water in the dark or will you  *wait*  to check your surroundings in the sunrise?   ")
    print(second_choice)
    second_choice = second_choice.lower()

    if second_choice == "wait":
        third_choice = input("You waited for the morning, and once the sun came up you are able to see a small bridge in the distance. You crossed the bridge and continued on the path. You now see a small masoleum with three doors:  *red*,  *blue*,  and  *yellow*.  Or will you  *leave*  well enough alone despite the promise of life-, no GENERATION-changing wealth? You do have a 33% chance of success if you open a door...which door will you enter?   ")
        print(third_choice)
        third_choice = third_choice.lower()
    
        if third_choice == "yellow":
            print("You chose the yellow door. The particular shade of pale, nearly white, yellow reminds you of the new path you've chosen in your life. Yellow is the color of determination. Yellow is also the color of gold...which you found piled in the room like the galleons in Harry Potter's bank vault. You Win!")
        elif third_choice == "red":
            print("You chose the red door because it reminded you of flames burning in a fall bonfire in November. This was your first first date as a teen, with the one who is now your soul mate. Once you openeded the door, the door (and you) burst into flames. Game Over.")
        elif third_choice == "blue":
            print("You chose the blue door because blue is a cool tone and helps to calm you down. After you opened the door, three large beasts emerged from the darkness and attacked you. Game Over.")
        else:
            print("You decided to leave the masoleum; the sense of anger and danger surrounded the building like an aura. You might not have found the treasure...but you survided another day.")

    else:
        print("You decided to take a nighttime swim...and from the depths a trout the size of a whale zoomed to you and attacked your toes. On both feet. Game Over.")

else:
     print("You took one step on the path to the right, immediately fell into a hole, ...and sprained your ankle. Game Over.")


