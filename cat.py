class Cat():

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def eat(self):
        print(f'{self.name} eats the food.')
        self.purr

    def sleep(self):
        print(f'{self.name} is sleeping. Maybe try again later.')

    def hiss(self):
        print(f'{self.name} hisses! Maybe try again later.')

    def purr(self):
        print(f'{self.name} purrs loudly.')