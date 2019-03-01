#Hangman Game
import time
import getpass

while True:
    try:
        word = getpass.getpass("Player 1, pick a word (type 'exit' to leave):")
        if word == 'exit':
            print("===== It was fun user, goodbye! <3 =====")
            break
        orig_quess_num = input("Set number of quesses (Note the original is 6):")
        orig_quess_num = int(orig_quess_num)
        quess_num = orig_quess_num
        check=word
        times=0
        name=list()
        #wait 2s for Player 2
        print("Player 2, are you ready?")
        time.sleep(1)
        print("The game is ON!\n")
        time.sleep(1)
        #create a list of underscores
        for i in range(len(word)):
            name.append("_")
        while quess_num > 0:
            #First print
            if times == 0:
                print("\n======================================")
                print("You must quess a", len(word),"letter word.")
                times+=1
                print("======================================")
                for i in name:
                    print(i, sep ='', end =' ')
                print()
            letter = input("Player 2, please quess a letter:")
            try:
                if len(letter) != 1:
                    if letter == word and quess_num>0:
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
                if letter not in word and len(letter) == 1:
                    quess_num -=1
                    print("\n===== Sorry, wrong quess!")
                    print("===== You have", quess_num, "quesses left!")
                    if orig_quess_num == 6 and quess_num == 5:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 4:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  |      |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 3:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 2:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 1:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('  /      |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 0:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('  / \    |')
                        print('         |')
                        print(' ========|')
                        print("\n===== You have", quess_num, "quesses left!")
                        print("\n\n============== You lose! ==============")
                        print("        The word was:",word+"!         ")
                        print("=======================================")

                    if quess_num==0:
                        print("\n\n=======================================")
                        print("============== You lose! ==============")
                        print("        The word was:",word+"!         ")
                        print("=======================================")
                #Finds all indecies for quessed letter in word
                elif letter in word and len(letter) == 1:
                    indecies= [index for index, value in enumerate(word) if value == letter]
                    # print(indecies)
                    for index in indecies:
                        name[index]=letter
                    #Just count the remaining letters
                    check=check.replace(letter,"")
                    print("\n===== Correct quess!",len(check),"letters remaining!")
                    # print("   "+("_ "*len(word)))
                    for i in name:
                        print(i, sep='', end=' ')
                    print()
                    if orig_quess_num == 6 and quess_num == 5:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 4:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  |      |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 3:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('         |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 2:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('         |')
                        print('         |')
                        print(' ========|')
                        print("===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 1:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('  /      |')
                        print('         |')
                        print(' ========|')
                        print("===== You have", quess_num, "quesses left!")
                    elif orig_quess_num == 6 and quess_num == 0:
                        print('   ______')
                        print('   |     |')
                        print('   @     |')
                        print('  | |    |')
                        print('   |     |')
                        print('  / \    |')
                        print('         |')
                        print(' ========|')
                    if len(check) == 0 and quess_num>0:
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
