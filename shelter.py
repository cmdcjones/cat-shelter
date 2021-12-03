class Shelter():

    MAX_CATS = 10
    cat_database = []

    def __init__(self):
        print('Welcome to the Cat Shelter!')

    def admit_cat(self, cat_name=''):
        self.name = cat_name
        self.cat_database.append(cat_name)

    def adopt_cat(self, cat_name, owner_name):
        self.cat_name = cat_name
        self.owner_name = owner_name
        for cat in range(len(self.cat_database)):
            if self.cat_name.lower() == self.cat_database[cat].lower():
                print(f'Thank you, {self.owner_name}!! \
You\'ve given {self.cat_database[cat]} a happy home!\n')
                return self.cat_database.pop(cat)
        return print("That cat does not exist in the database!\n")

    def feed_cat(self, cat_name):
        self.cat_name = cat_name
        print(f'Feeding {self.cat_name} some food.\n')

    def bathe_cat(self, cat_name):
            self.cat_name = cat_name
            print(f'Attempting to bathe {self.cat_name}... This may not end well.')

    def select_cat(self):
        self.cat_selection = input(f"Select a cat from the database: \n\
" + ", ".join(self.cat_database) + "\n> ")
        for cat in range(len(self.cat_database)):
            if self.cat_selection.lower() == self.cat_database[cat].lower():
                return self.cat_database[cat]
        else:
            print("That cat does not exist in the database!")
            self.select_cat()

    def view_database(self):
        print("Viewing all cats in the database:")
        print(", ".join(self.cat_database))