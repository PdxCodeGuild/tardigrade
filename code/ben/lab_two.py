# Mad Libs

# from xml.dom.expatbuilder import makeBuilder

# Mad Lib Lab - Ben Morgan

while True: 
    x,y,z= input("Enter three adjectives separated by commas: ").split(",",3)
    location = input("Enter a location: ")
    state = input("Enter a state: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    verb_two = input("Enter a verb: ")
    item = input("Enter as item: ")
    noun_two = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adjective_two = input("Enter an adjective: ")
    adjective_three = input("Enter an adjective: ")
    vehicle = input("Enter a vehicle: ")
    place = input("Enter a place: ")
    action = input("Enter an action: ")
    command = input("Enter a command: ")
    animal = input("Enter an animal: ")

    mad_libs = f"""
    While at a {x} {location} in {state}, I went to {y} {noun} and {verb} by a gentleman who {verb_two} on the phone. 
    I overheard him say that he had “lost {item} yesterday” because his “{noun_two} got {adjective}” 
    so he “stopped at a {adjective_two} stop and hosed them down with {adjective_three}water.” 
    Then I noticed a school {vehicle} in front of the {place} that hadn’t been there the day before. 
    When the gentleman ended his {action}, I asked him if that was his bus. “{command},” he replied. 
    “I’m in the back with a semi load of {z} {animal}.”
    """

    hear_story = input("Would you like to hear the story? (y/n) ").lower()
    if hear_story == "y":
        print(mad_libs)
        new_story = input("Would you to play again? (y/n) ").lower()
        if new_story == "y":
            continue
        elif new_story == "n":
            break
    elif hear_story == "n":
        break
    else:
        print("Invalid Response. Please Run Again")
        break