# Cat Shelter project - Be in charge of a cat shelter! Admit, feed, bathe, and put cats up for adoption!
# Concepts used: imports, classes, functions, class attributes, methods, user input, lists, loops, conditionals, standard modules (random)
# ----------------------------------------------------------------------------------------------------------------------------------------
# TODO:
# file handling, exception handling, more features

from shelter import Shelter
from cat import Cat
import sys

def main():
    shelter = Shelter()
    current_cat = Cat()

    while True:
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
            cat_name = input("What is the cat's name?  ")
            shelter.admit_cat(cat_name)
        if action == '2':
            if not shelter.cat_database:
                continue
            owner_name = input("What is your name?  ")
            adopt_cat_name = input("What lucky cat would you like to adopt?  ")
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
            current_cat.behavior()
        if action == '5':
            if not shelter.cat_database:
                continue
            shelter.view_database()
        if action == '6':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()