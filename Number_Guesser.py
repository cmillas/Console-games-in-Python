import random
version = '1.0.0'
creator ='Christos Millas'
time = 'February 2019'

print('Created by {} in {}, version: {}\n\n'.format(creator, time, version))

header= '''Hello user! This is a game of chance!
Guess what number I think of and you win!
-----------------------------------------\n'''

print(header)
randomNumber = random.randint(1,10)
while True:
    inp = input("Guess an integer number between 1 and 10:")
    try:
        if inp.upper() == "Q":
            print('\nGoodbye user, it was a pleasure!')
            break
        guess = int(inp)
        if randomNumber != guess:
            print("Wrong guess\n")
        elif randomNumber == guess:
            print("Yeah, you are correct!!\n")
            print("-----------------------\n")
            ask = input("Do you want to play again (Y or N)?")
            if ask.upper() == "Y":
                continue
            elif ask.upper() == "N":
                print('\nGoodbye user, it was a pleasure!')
                break
            else:
                print(" I don't like stupid people!!! Bye!")
                break
    except ValueError:
        print("This is not a number\n")
    except:
       print("Something gone terribly wrong\n")