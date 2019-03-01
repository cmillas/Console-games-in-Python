#Hangman Game
import time
import getpass

def hang(guess_num):
    ''' return a graphic representation of the hang'''
    if guess_num == 5:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print(' ========|')
        print("===== You have", guess_num, "guesses left!")
    elif guess_num == 4:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('  |      |')
        print('         |')
        print('         |')
        print('         |')
        print(' ========|')
        print("===== You have", guess_num, "guesses left!")
    elif guess_num == 3:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('  | |    |')
        print('         |')
        print('         |')
        print('         |')
        print(' ========|')
        print("===== You have", guess_num, "guesses left!")
    elif guess_num == 2:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('  | |    |')
        print('   |     |')
        print('         |')
        print('         |')
        print(' ========|')
        print("===== You have", guess_num, "guesses left!")
    elif guess_num == 1:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('  | |    |')
        print('   |     |')
        print('  /      |')
        print('         |')
        print(' ========|')
        print("===== You have", guess_num, "guesses left!")
    elif guess_num == 0:
        print('   ______')
        print('   |     |')
        print('   @     |')
        print('  | |    |')
        print('   |     |')
        print('  / \    |')
        print('         |')
        print(' ========|')
        print("\n===== You have", guess_num, "guesses left!")
        print("\n\n============== You lose! ==============")
        print("        The word was:", word + "!         ")
        print("=======================================")

def name_print(name):
    print()
    for i in name:
        print(i, sep='', end=' ')
    print()

def wrong_print(wrong):
    print("\nYou already guessed wrong:")
    for j in wrong:
        print(j, sep=' , ', end=' ')
    print()


while True:
    try:
        word = getpass.getpass("Player 1, pick a word (type 'exit' to leave):")
        if word == 'exit':
            print("===== It was fun user, goodbye! <3 =====")
            break
        orig_guess_num = input("Set number of guesses (Note the original is 6):")
        orig_guess_num = int(orig_guess_num)
        guess_num = orig_guess_num
        check=word
        times=0
        name=list()
        wrong = list()
        #wait 2s for Player 2
        print("Player 2, are you ready?")
        time.sleep(1)
        print("The game is ON!\n")
        time.sleep(1)
        #create a list of underscores
        for i in range(len(word)):
            name.append("_")
        while guess_num > 0:
            #First print
            if times == 0:
                print("\n======================================")
                print("You must guess a", len(word),"letter word.")
                times+=1
                print("======================================")
                name_print(name)
                wrong_print(wrong)
            letter = input("Player 2, please guess a letter:")
            try:
                if len(letter) != 1:
                    if letter == word and guess_num>0:
                        print("\n======================================")
                        print("============== You win! ==============")
                        print("======================================")
                        break
                    else:
                        print("\n=======================================")
                        print("======= Wrong guess, you lose! ========")
                        print("        The word was:",word+"!         ")
                        print("=======================================")
                        break
                if letter in wrong:
                    continue
                elif letter not in word and len(letter) == 1:
                    guess_num -= 1
                    wrong.append(letter)
                    print("\n===== Sorry, wrong guess!")
                    print("===== You have", guess_num, "guesses left!")
                    print()
                    name_print(name)
                    wrong_print(wrong)
                    if orig_guess_num == 6:
                        hang(guess_num)

                    if orig_guess_num != 6 and guess_num == 0:
                        print("\n\n=======================================")
                        print("============== You lose! ==============")
                        print("        The word was:",word+"!         ")
                        print("=======================================")
                #Finds all indecies for guessed letter in word
                elif letter in word and len(letter) == 1:
                    indecies= [index for index, value in enumerate(word) if value == letter]
                    # print(indecies)
                    for index in indecies:
                        name[index]=letter
                    #Just count the remaining letters
                    check=check.replace(letter,"")
                    print("\n===== Correct guess!",len(check),"letters remaining!")
                    # print("   "+("_ "*len(word)))
                    name_print(name)
                    wrong_print(wrong)
                    if orig_guess_num == 6:
                        hang(guess_num)

                    if len(check) == 0 and guess_num>0:
                        print("\n======================================")
                        print("============== You win! ==============")
                        print("======================================")
                        break
            except KeyboardInterrupt:
                print("\n===== Swore loser! You killed me :( =====")
    except KeyboardInterrupt:
        print("\n\n===== YOU SAVAGE! You killed me :'( =====")
        break
    except:
        print("\n===== Wrong Input! =====")
        continue


