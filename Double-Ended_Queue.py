print('======================================================================')
print('========================= Double-Ended Queue =========================')
print('======================================================================')
print('====================================================================== \n')

print('Hi there, user!')
start='''Το σύστημα θα κατασκευάσει μια λίστα L με αριθμούς ή γράμματα που όμως
θα αποθυκεύονται ως αλφαριθμητικά στοιχεία. Τα στοιχεία που θα λάβει η
λίστα θα εισάγωνται τελευταία. Όταν ο χρήστης εισάγει την εντολή με
πρόθεμα 0 (π.χ. 015), τότε τα στοιχεία θα προστεθούν ως πρώτα στη λίστα.
Με την εντολή r θα αφαιρείται το τελευταίο στοιχείο της λίστας και αντί-
στοιχα με 0r το πρώτο στοιχείο. Με την εντολή q ο χρήστης αποχωρεί.'''
print(start)

l=[]
inp=None

while True:
    inp=input('\nΓια νέο στοιχείο n/Για αφαίρεση στοιχείου r ή 0r/Για έξοδο q: ')
    if inp=='r':
        l.pop()
        print('\nL= ',l)
    elif inp.startswith('0'):
        if inp=='0r':
            l.pop(0)
            print('\nL= ',l)
        else:
            inp=inp[1:len(inp)]
            inp=int(inp)
            l.insert(0,inp)
            print('\nL= ',l)
    elif inp=='q':
        break
    else:
        inp=int(inp)
        l.append(inp)
        print('\nL= ',l)

end='''\n======================================================================\n\
================== Τέλος Λίστας. Χρήστη σε Χαιρετώ!! =================\n\
======================================================================'''
print(end)
