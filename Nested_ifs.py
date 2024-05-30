# Task 1/2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    explore = input("light a torch or proceed in the dark?")
    if explore == "light a torch":
        print("Yikes the spiders!")
    elif explore == "proceed in the dark":
        print("I can't see, lets hope I don't trip!")

#Task 3

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    explore = input("light a torch or proceed in the dark?")
    if explore == "light a torch":
        print("Yikes the spiders!")
    elif explore == "proceed in the dark":
        print("I can't see, lets hope I don't trip!")
