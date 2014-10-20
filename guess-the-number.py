from random import randint

min,max = 1,6

random_number = randint(min,max)



choice = int(input('Please guess the number:'))

if(isinstance(choice,int)):
    if(choice>random_number):
        print("Too Large Number")
        exit()
    else:
        print('Too Small Number')
        exit()
else:
    print('Wrong input:')
