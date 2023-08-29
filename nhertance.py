class Animal:
    def walk(self):
        print('walking')

class Dog (Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('barking')

buntu = Dog('buntu', 56)

print(buntu.name)
print(buntu.age)

buntu.bark()
buntu.walk()
