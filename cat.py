import random

class Cat():

    def __init__(self, name=''):
        self.name = name

    def eat(self):
        print(f'{self.name} eats the food.\n')
        self.purr()

    def purr(self):
        print(f'{self.name} purrs loudly.\n')
    
    def behavior(self, cat_name):
        self.name = cat_name
        self.behavior_ = random.randint(0, 2)
        if self.behavior_ == 0:
            print(f'{self.name} is sleeping. Maybe try again later.\n')
        elif self.behavior_ == 1:
            print(f'{self.name} hisses! Maybe try again later.\n')
        else:
            self.purr()