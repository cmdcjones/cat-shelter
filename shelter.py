class Shelter():

    MAX_CATS = 10
    cat_database = []

    def __init__(self):
        print('Welcome to the Cat Shelter!')

    def admit_cat(self, cat_name=''):
        if len(self.cat_database) == self.MAX_CATS:
            return print('The Cat Shelter is full at this time. \
More cats must be adopted first!')
        self.name = cat_name
        self.cat_database.append(cat_name)

    def adopt_cat(self, cat_name, owner_name):
        self.cat_name = cat_name
        self.owner_name = owner_name
        if self.cat_name in self.cat_database:
            print(f'Thank you, {self.owner_name}!! \
You\'ve given {self.cat_name} a happy home!')
        else:
            return print("That cat does not exist in the database!")
        for cat in self.cat_database:
            if cat.lower() == self.cat_name.lower():
                self.cat_database.remove(cat)

    def feed_cat(self, cat_name):
        self.cat_name = cat_name
        print(f'Feeding {self.cat_name} some food.')

    def bathe_cat(self, cat_name):
            self.cat_name = cat_name
            print(f'Attempting to bathe {self.cat_name}... This may not end well.')

    def select_cat(self):
        self.cat_selection = input(f"Select a cat from the database: \n\
" + ", ".join(self.cat_database) + "\n> ")
        if self.cat_selection in self.cat_database:
            return self.cat_selection
        else:
            print("That cat does not exist in the database!")
            self.select_cat()

    def view_database(self):
        print("Viewing all cats in the database:")
        print(", ".join(self.cat_database))
    