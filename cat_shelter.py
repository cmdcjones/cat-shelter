# Cat Shelter project - Be in charge of a cat shelter! Admit, feed, bathe, and put cats up for adoption!
# Concepts used: imports, classes, functions, class attributes, methods, user input, lists, loops, conditionals, standard modules (random)
# ----------------------------------------------------------------------------------------------------------------------------------------
# TODO:
# exception handling, more features (file handling) ... soon

from shelter import Shelter
from cat import Cat
import sys

def main():
    shelter = Shelter()
    current_cat = Cat()

    while True:
        # Message displaying the shelter is empty; replayed when the shelter is empty after choosing a menu action
        if not shelter.cat_database:
            print("The Cat Shelter is empty! \
Let's find more cats to take care of.")
        action = input("""What would you like to do?

1 - Admit a new cat
2 - Adopt a cat
3 - Feed a cat
4 - Bathe a cat
5 - View the cat database
6 - Exit

> """)
        if action == '1':
            # Checks if the shelter is full; MAX_CATS = 10
            if len(shelter.cat_database) == shelter.MAX_CATS:
                print('The Cat Shelter is full at this time. \
More cats must be adopted first!\n')
                continue
            cat_name = input("What is the cat's name?\n> ")
            # Checks for accidental double enter input; continues loop if true 
            if cat_name.strip() == '':
                continue
            shelter.admit_cat(cat_name.title())
        if action == '2':
            if not shelter.cat_database:
                continue
            owner_name = input("What is your name?\n> ")
            adopt_cat_name = input("What lucky cat would you like to adopt?\n\
" + ", ".join(shelter.cat_database) + "\n> ")
            shelter.adopt_cat(adopt_cat_name, owner_name)
        if action == '3':
            if not shelter.cat_database:
                continue
            current_cat.name = shelter.select_cat()
            shelter.feed_cat(current_cat.name)
            current_cat.purr()
        if action == '4':
            if not shelter.cat_database:
                continue
            current_cat.name = shelter.select_cat()
            shelter.bathe_cat(current_cat.name)
            # Don't get hissed at!
            current_cat.behavior(current_cat.name)
        if action == '5':
            if not shelter.cat_database:
                continue
            shelter.view_database()
        if action == '6':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()