# This is the first Python program
print(2+2)
print(2**3) #指数
print(22%5) #取模
print(22/8) #除法
print(22//8) #整除/取整
print('Allen'*5) #字符串复制

#Test Input
# print('Input your name below and press \'ENTER\' ')
# name = input()
# print('Hello ' + name)
# print('The length of your name is ' + str(len(name)))

#Guess a Number
# key = 101
# while(1):
#     guess = int(input())
#     if(guess > key):
#         print('too big')Allen
#     elif(guess < key):
#         print('too small')
#     else:
#         print('Biggo!!!')
#         break

#Test Boolean
print(True and False)
print(True or False)

#Test loop
spam = 0
while spam < 10 :
    print('  '*(20-spam) + 'spam' * spam)
    spam = spam + 1

for i in range(12,26,3):
    print(i)