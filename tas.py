name = 'the way is not clear'
print(name[5:])

num = complex(2,5)

print(num.real , num.imag)


done = input('Enter any number : ')

if done :

    print('positive')

else :
    print('negative')

from enum import Enum

class buntu(Enum):
    active = 20
    inactive = 40

print (buntu.active.value, buntu.inactive.value,)

dog = {"name":"Max", "age":30 , "colour":"black"}

print(dog.get('name'))
print("age" in dog)
print(dog.keys())
print(dog.values())
print(dog.items())
print(len(dog))

del dog["colour"]
dogCopy = dog.copy()
print(dog)
print(dogCopy)
# dog.update(['name', 'blue'])
# print(dog)


def hello(name1 = 'u didnt provide a name'):
    print(f"Hello {name1}")

hello('qween')
hello()

def talk(phrase):
    def say(word):
        print(word)


    words = phrase.split(' ')
    number = 0
    for word in words:
        number = number + 1
        say(word)
    print(number)
    # return number


talk('l am not who you think you are based on the fact that l love ')

#objects
age = 7
print(age.bit_length)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
items.append(99)
print( items)
print( items.pop())
print(id(items))
