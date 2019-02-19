print('========================================================================')
print('===========================  Dictionary  ===============================')
print('==================== powered by Christos Millas ========================')
print('======================================================================== \n')

print('Hi there, user!')
start='''By inserting the ID and the name (separated by ','), a dictionary will be constructed, sorted by ID number.
Enter q to quit'''
print(start)

ID=[]
NAME=[]
while True:
    inp=input('\nInsert ID and name, separatedd by "," (q to exit): ')
    if inp.lower()=='q':
        try:
            for i in sorted(di):
                print('\nDictionary:')
                print('ID','\t Name\n--------------------')
                print(i, '\t', di[i])
            break
        except:
            break
    else:
        try:
            lista=inp.split(',')
            am=int(lista[0])
            name=lista[1]
            ID.append(am)
            NAME.append(name)
            di=dict(zip(ID,NAME))
            print('\nDictionary:')
            print('ID', '\t Name\n____________________')
            for i in sorted(di):
                print(i,'\t', di[i])
        except ValueError:
            print("Wrong input, try again")


end='''\n======================================================================\n\
========================= Goodbye User!! ========================\n\
======================================================================'''
print(end)
