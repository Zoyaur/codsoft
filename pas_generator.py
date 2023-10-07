import random
chars="abcdefghijklmnopqrstuvwxyz1234567890._,@#$&!+-*/"
#user can decide the length of the password
length=int(input("enter the length of the password"))
#an empty variable name password created to store random generated password
password=""
#for loop takes the round on the basis of range of decided lenght by user
for a in range(length):
    #random function is used here for generating random numbers between 0 and len(chars) -1
    password=random.choice(chars)
    #end='' argument used to make the function print ,print the output horizontally 
    print( password , end='')
