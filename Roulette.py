print('=====================================================================')
print('============================ Roulette ===============================')
print('=====================================================================')
print('===================================================================== \n')

print('Hi there, user! \n')
#Εισαγωγή βιβλιοθήκης Random
import random as rn
#Εντολή για νέα κλήρωση ή αποχώρηση
a='''=====================================================================
Για νέα κλήρωση εισάγετε το γράμμα N, για έξοδο εισάγετε το γράμμα Q!
====================================================================='''
print(a)
Command=input('Εισάγετε την εντολή σας: ')
while Command not in ['N','n','ν','Ν','Q','q']:
    Command=input('Χαζούλη προσπάθησε πάλι: ')
else:
    #Loop για Μέγεθος,Χρώμα, Είδος
    while Command in ('N','n','Ν','ν'):
        f=rn.randrange(0,37,1)
        if f==0:
            print('\nΚληρώθηκε ο αριθμός 0', end='\n')
            print('\n=====================================================================\n=====================================================================\n')
        elif 1<=f<=17:
            size='Μικρός'
            if 1<=f<=10 and f%2!=0:
                color='Κόκκινο'
                eidos='Μονός'
            elif 1<=f<=10 and f%2==0:
                color='Μαύρο'
                eidos='Ζυγός'
            elif 11<=f<18 and f%2!=0:
                color='Μαύρο'
                eidos='Μονός'
            elif 11<=f<18 and f%2==0:
                color='Κόκκινο'
                eidos='Ζυγός'
        elif f>=18:
            size='Μεγάλος'
            if f==18:
                color='Κόκκινο'
                eidos='Ζυγός'
            elif 19<=f<=28 and f%2!=0:
                color='Κόκκινο'
                eidos='Μονός'
            elif 19<=f<=28 and f%2==0:
                color='Μαύρο'
                eidos='Ζυγός'
            elif 29<=f<=36 and f%2!=0:
                color='Μαύρο'
                eidos='Μονός'
            elif 29<=f<=36 and f%2==0:
                color='Κόκκινο'
                eidos='Ζυγός'
        print('\nΚληρώθηκε ο',eidos,'αριθμός: ',f,'\nΧρώμα:',color,end='\n')
        print('Μέγεθος:',size,end='\n')
        print('\n=====================================================================\n=====================================================================\n')
        #Επανάληψη κλήρωσης ή αποχώρηση
        if Command not in ['N','n','ν','Ν','Q','q']:
            Command=input('Χαζούλη προσπάθησε πάλι: ')
        else:
            print(a)
            Command=input('Εισάγετε την εντολή σας: ')             



b='''\n=====================================================================\n\
======================= Χρήστη σε Χαιρετώ ===========================\n\
====================================================================='''
print(b)