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

print (buntu.active.value)
