class Shelter():

    MAX_CATS = 10
    cat_database = []

    def __init__(self):
        print('Welcome to the Cat Shelter!')

    def admit_cat(self, cat_name=''):
        if len(self.cat_database) == self.MAX_CATS:
            print('The Cat Shelter is full at this time. \
More cats must be adopted first!')
        self.name = cat_name
        self.cat_database.append(cat_name)

    def adopt_cat(self, cat_name, owner_name):
        self.cat_name = cat_name
        for cat in self.cat_database:
            if cat == cat_name:
                self.cat_name = cat_name
        self.owner_name = owner_name
        print(f'Thank you, {self.owner_name}!! \
You\'ve given {self.cat_name} a happy home!')

    def feed_cat(self, cat_name):
        self.cat_name = cat_name
        print(f'Feeding {self.cat_name} some food.')

    