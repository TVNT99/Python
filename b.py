from random import randint
player = input()

computer = randint(0,2)
if computer == 0:
	computer = "keo"
if computer == 1:
	computer ="bua"
if computer == 2: 
	computer = "bao"
print(computer)
if player == computer:
	print("draw")

elif player == "keo":
	if computer =="bua":
		print("lose")
	if computer =="bao":
		print("win")
elif player == "bao":
	if computer == "keo":
		print("lose")
	if computer == "bua":
		print ("win")
elif player == "bua":
	if computer == "bao":
		print("lose")
	if computer == "keo":
		print("win")

