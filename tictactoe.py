import random
import os
import time
#Create board
board =[" "," "," "," "," "," "," "," "," "," "]

#print board function
def print_board():
	print "    |    |    "
	print " "+board[1]+"  |  "+board[2]+" |  "+board[3]+" "
	print "    |    |    "
	print " ---|----| --- "
	print "    |    |    "
	print " "+board[4]+"  |  "+board[5]+" |  "+board[6]+" "
	print "    |    |    "
	print " ---|----| --- "
	print "    |    |    "
	print " "+board[7]+"  |  "+board[8]+" |  "+board[9]+" "
	print "    |    |    "
numbers = [1,2,3,4,5,6,7,8,9]
#Main Loop
while True:
	os.system("CLS")
	print_board()
	
	#Make choice loop
	while True:
		choice = raw_input("Input a value between 1 and 9 to insert an X mark:  ")
		choice = int(choice)
		#Check if space is empty
		if board[choice] == " ":
			board[choice] = "X"
			break
		else:
			print "Try another space, block %d is already filled" %choice
			time.sleep(2)
	#Check if X wins
	if board[1]== "X" and board[2] == "X" and board[3] == "X" or\
		board[4]== "X" and board[5] == "X" and board[6] == "X" or\
		board[7]== "X" and board[8] == "X" and board[9] == "X" or\
		board[1]== "X" and board[4] == "X" and board[7] == "X" or\
		board[2]== "X" and board[5] == "X" and board[8] == "X" or\
		board[3]== "X" and board[6] == "X" and board[9] == "X" or\
		board[1]== "X" and board[5] == "X" and board[9] == "X" or\
		board[3]== "X" and board[5] == "X" and board[7] == "X":
		os.system("CLS")
		print_board()
		print "Congratulations! You Win!!"
		break
	
	#Determine allowed boxes for AI to play
	
	if choice in numbers:
		numbers.remove(choice)
		
	#Set criteria for a draw
	if len(numbers)==0:
		
		os.system("CLS")
		print_board()
		print "It's a DRAW! There are no more spaces to play"
		break
		
		
	#AI
	
	#AI check for win or prevent loss
	while len(numbers)>0:
		AI_choice = random.choice(numbers)
		if board[AI_choice]== " ":
			board[AI_choice] = "O"
			numbers.remove(AI_choice)
			break
		
	
	#Check if AI wins
	if board[1]== "O" and board[2] == "O" and board[3] == "O" or\
		board[4]== "O" and board[5] == "O" and board[6] == "O" or\
		board[7]== "O" and board[8] == "O" and board[9] == "O" or\
		board[1]== "O" and board[4] == "O" and board[7] == "O" or\
		board[2]== "O" and board[5] == "O" and board[8] == "O" or\
		board[3]== "O" and board[6] == "O" and board[9] == "O" or\
		board[1]== "O" and board[5] == "O" and board[9] == "O" or\
		board[3]== "O" and board[5] == "O" and board[7] == "O":
		os.system("CLS")
		print_board()
		print "Too Bad! You Lost!!"
		break
	