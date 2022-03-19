import string
import random as random
#importing libraries
try:#putting it on to the try to not get error when we stop this code
    char = list(string.ascii_letters + string.digits + "+-*/#@!") #the list of the symbols that we are going to make our password
    while True:
        
            limit = int(input("pls enter the maximum char limit")) #inputting the maximum letter in the password
            random.shuffle(char) #shuffling the list
            password = [] #creating a password list that we are going to append
            for i in range(limit):
                password.append(random.choice(char)) 
            random.shuffle(password)
            print("".join(password))
        
            
except KeyboardInterrupt: #if we press control + c it will give this sentence
    print(" exited \n")
   
