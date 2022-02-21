while True:
	x = int(input("pls enter the first number"))## getting the first input to calculate
	opt = input("pls enter the operation you want to do")# the person is inputting what will they do with the integers(+-*/)
	y = int(input("pls enter the first number"))##getting the second input to calculate
def calc(x,y,opt):
	if opt not in "/*-+":
		return("choose avaliable option")
	elif(opt == "*"):
		return(str(x) + opt + str(y) + " =" +str(x*y))
	elif(opt == "-"):
		return(str(x) + opt + str(y) + " =" +str(x-y))
	elif(opt == "+"):
		return(str(x) + opt + str(y) + " =" +str(x+y))
	elif(opt == "/"):
		return(str(x) + opt + str(y) + " =" +str(x/y))
