print('=========================================================================================')
print('========================= Quadratic Equation - Root Calculator ==========================')
print('=========================================================================================')
print('========================================================================================= \n')

print('Hi there, user! \n')

g='''Εισάγετε στο σύστημα τις σταθερές α,β,γ της δευτεροβάθμιας εξίσωσης της μορφή αχ**2+βχ+γ.
Οι σταθερές πρέπει να ανήκουν στο R (πραγματικοί αριθμοί).'''
print(g)
a=float(input('Εισάγετε σταθερά α : '))
b=float(input('Εισάγετε σταθερά β : '))
c=float(input('Εισάγετε σταθερά γ : '))

import math as m
#(a*x**2)+b*x+c=0
#x=(-b+-m.sqrt(Δ)/2*a
#Δ=(b**2-(4*a*c)

if (b**2-(4*a*c))>0:
    x1=(-b + m.sqrt(b**2-(4*a*c)))/(2*a)
    x2=(-b - m.sqrt(b**2-(4*a*c)))/(2*a)
    print('Οι πραγματικές λύσεις είναι: ','\t x1= ',x1 ,\
          '\n\t\t\t\t x2= ',x2)
    
elif (b**2-(4*a*c))==0:
    x= (-b)/2*a
    print('Οι πραγματικές λύσεις είναι: '+'\t x= ',x)
else:
    print('Δεν υπάρχουν πραγματικές ρίζες')

print('\n==========================================================================================')
print('============================== You are welcome ===========================================')
print('==========================================================================================')

