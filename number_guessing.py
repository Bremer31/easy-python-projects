import random 
#importing library
r1 = random.randint(0, 100)# r1 = a random integer that is between in 0 and 100


while True:
	x = int(input("pls enter your guess"))# a integer input
	if x >r1:
		print("lower your number")
	elif x < r1:
		print("pls increase your number")
	elif x == r1:
		print('YOU GOT THE CORRECT ANSWER')
		break

