class Shelter():

    MAX_CATS = 10
    cat_database = []

    def __init__(self):
        # Greets user and opens the shelter for business!
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
        # if inputted cat is not in the database, return user a message
        return print("That cat does not exist in the database!\n")

    def feed_cat(self, cat_name):
        self.cat_name = cat_name
        print(f'Feeding {self.cat_name} some food.')

    def bathe_cat(self, cat_name):
            self.cat_name = cat_name
            print(f'Attempting to bathe {self.cat_name}... This may not end well.')

    def select_cat(self):
        while True:
            self.cat_selection = input(f"Select a cat from the database: \n\
" + ", ".join(self.cat_database) + "\n> ")
            for cat in range(len(self.cat_database)):
                # uses lower() function to compare strings in identical format
                if self.cat_selection.lower() == self.cat_database[cat].lower():
                    return self.cat_database[cat]
            else:
                print("That cat does not exist in the database!")

    def view_database(self):
        print("Viewing all cats in the database:")
        print(", ".join(self.cat_database))