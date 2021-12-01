# Cat Shelter project
# Concepts used: imports, classes, functions, class attributes, methods, user input, lists, loops, conditionals, standard modules (random)
# ----------------------------------------------------------------------------------------------------------------------------------------
# TODO:
# file handling, exception handling, more features

from shelter import Shelter
from cat import Cat
import sys

def main():
    while True:
        shelter = Shelter()
        if not shelter.cat_database:
            print("The Cat Shelter is empty! \
Let's find more cats to take care of.")
        action = input("""What would you like to do?

        1 - Admit a new cat
        2 - Adopt a cat
        3 - Feed a cat
        4 - Bathe a cat
        5 - Exit
        
        > """)
        if action == '1':
            cat_name = input("What is the cat's name?  ")
            cat_age = input(f"What is {cat_name}'s age?  ")
            cat_breed = input(f"What is {cat_name}'s breed?  ")
            new_cat = Cat(cat_name, cat_age, cat_breed)
            shelter.cat_database.append(new_cat.get_name)
        if action == '2':
            if not shelter.cat_database:
                continue
            owner_name = input("What is your name?  ")
            adopt_cat_name = input("What lucky cat would you like to adopt?  ")
            shelter.adopt_cat(adopt_cat_name, owner_name)
        if action == '5':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()