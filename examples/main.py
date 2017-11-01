import utilities
import jw_utils

menuSystem = jw_utils.helpers.menu.Menu("Score Tracker Program")

def show_all_scores():
    print()
    f = utilities.getFile()
    for i, entry in enumerate(f):
        if (i % 2) == 1: continue
        print(f[i] + " (" + str(f[i+1]) + ")")
    print()
menuSystem.addOption("Show all scores", show_all_scores)

def find_a_score():
    print()
    toFind = input("Who's score do you want to find? >")
    f = utilities.getFile()
    ind = utilities.findNameIndex(toFind, f)
    print("\n" + f[ind] + "'s score is " + str(f[ind+1]))
    print()
menuSystem.addOption("Find a score", find_a_score)

def add_a_score():
    print()
    name = input("name>")
    score = input("score>")
    utilities.addPerson(name, score)
    print(jw_utils.unicode.emoji.symbols.tick + " Added.")
    print()
    print()
menuSystem.addOption("Add a score", add_a_score)

def update_a_score():
    print()
    name = input("name>")
    score = input("new score>")
    f = utilities.getFile()
    ind = utilities.findNameIndex(name, f)
    if ind == False:
        print(jw_utils.unicode.emoji.symbols.cross + " Could not update.")
        print("Reason: Could not find name. Please try again and / or add the name.")
    else:
        f[ind + 1] = int(score)
        print(jw_utils.unicode.emoji.symbols.tick + " Updated.")
    print()
    print()
menuSystem.addOption("Update a score", update_a_score)

menuSystem.doMenu()