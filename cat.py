import random

class Cat():

    def __init__(self, name=''):
        self.name = name

    def eat(self):
        print(f'{self.name} eats the food.')
        self.purr()

    def purr(self):
        print(f'{self.name} purrs loudly.')
    
    def behavior(self, cat_name):
        self.name = cat_name
        self.sleep = 0
        self.hiss = 1
        self.behavior = random.randrange(0, 2)
        if self.behavior == 1:
            print(f'{self.name} is sleeping. Maybe try again later.')
        else:
            print(f'{self.name} hisses! Maybe try again later.')