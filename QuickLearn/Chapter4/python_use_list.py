# this is a new class to learn python list

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are :')
for name in catNames:
    print(' ' + name)