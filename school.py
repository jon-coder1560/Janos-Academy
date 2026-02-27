import time
import os

PASS_SCORE = 40

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def algebra():
	score = 0
	print("Welcome to Algebra class!")
	print("\nYou will be given 5 questions to answer each worth 10 points.")
	print("In order to pass, you must get a 40%")
	ready = input("Are you ready? (y/n) ")
	if ready.lower() == "y":
		print("\nGetting Ready...")
		time.sleep(5)
		clear()
		question1 = int(input("Solve: 2x = 10: "))
		if question1 == 5:
			score += 10
		else:
			score -= 5

		question2 = int(input("\nSolve: x + 7 = 12: "))
		if question2 == 5:
			score += 10
		else:
			score -= 5

		question3 = int(input("\nSolve: 3x = 21: "))
		if question3 == 7:
			score += 10
		else:
			score -= 5

		question4 = int(input("\nSolve: x - 4 = 6: "))
		if question4 == 10:
			score += 10
		else:
			score -= 5

		question5 = int(input("\nSolve: 5x = 25: "))
		if question5 == 5:
			score += 10
		else:
			score -= 5

		print(score)
		time.sleep(5)
	else:
		choice2 = input("\nOk. Would you like to {e}xit or {s}witch classes: ")
		match choice2:
			case "e":
				print("\nNow Exiting...")
				time.sleep(5)
			case "s":
				print("\nNow returning to main program...")
				time.sleep(3)
				clear()
				mainProgram()

def english():
	print("Welcome to Algebra class!")
	print("\nYou will be given 10 questions to answer each worth 10 points.")
	print("In order to pass, you must get an 80%")
	ready = input("Are you ready? (y/n) ")
	if ready.lower() == "y":
		print("\nGetting Ready...")
		time.sleep(5)
	else:
		choice2 = int(input("\nOk. Would you like to exit (-1) or choose a different class (0): "))
		match choice2:
			case -1:
				print("\nNow Exiting...")
				time.sleep(5)
			case 0:
				print("\nNow returning to main program...")
				time.sleep(3)
				clear()
				mainProgram()

def science():
	print("Welcome to Algebra class!")
	print("\nYou will be given 10 questions to answer each worth 10 points.")
	print("In order to pass, you must get an 80%")
	ready = input("Are you ready? (y/n) ")
	if ready.lower() == "y":
		print("\nGetting Ready...")
		time.sleep(5)
	else:
		choice2 = int(input("\nOk. Would you like to exit (-1) or choose a different class (0): "))
		match choice2:
			case -1:
				print("\nNow Exiting...")
				time.sleep(5)
			case 0:
				print("\nNow returning to main program...")
				time.sleep(3)
				clear()
				mainProgram()

def history():
	print("Welcome to Algebra class!")
	print("\nYou will be given 10 questions to answer each worth 10 points.")
	print("In order to pass, you must get an 80%")
	ready = input("Are you ready? (y/n) ")
	if ready.lower() == "y":
		print("\nGetting Ready...")
		time.sleep(5)
	else:
		choice2 = int(input("\nOk. Would you like to exit (-1) or choose a different class (0): "))
		match choice2:
			case -1:
				print("\nNow Exiting...")
				time.sleep(5)
			case 0:
				print("\nNow returning to main program...")
				time.sleep(3)
				clear()
				mainProgram()

def health():
	print("Welcome to Algebra class!")
	print("\nYou will be given 10 questions to answer each worth 10 points.")
	print("In order to pass, you must get an 80%")
	ready = input("Are you ready? (y/n) ")
	if ready.lower() == "y":
		print("\nGetting Ready...")
		time.sleep(5)
	else:
		choice2 = int(input("\nOk. Would you like to exit (-1) or choose a different class (0): "))
		match choice2:
			case -1:
				print("\nNow Exiting...")
				time.sleep(5)
			case 0:
				print("\nNow returning to main program...")
				time.sleep(3)
				clear()
				mainProgram()

def mainProgram():
	name = input("What is your name? ")
	print(f"\nHello {name.capitalize()}! Welcome JANOS Academy!")

	print("You have 5 classes to take today: \n\n(1) Algebra \n(2) English \n(3) Science \n(4) History \n(5) Health")
	subject = int(input("\nType the number to the class you would like to take first, or -1 to exit: "))

	match subject:
		case 1:
			print("Switching to your Algebra class...\n")
			time.sleep(3)
			clear()
			algebra()
		case 2:
			print("Switching to your English class...\n")
			time.sleep(3)
			english()
		case 3:
			print("Switching to your Science class...\n")
			time.sleep(3)
			science()
		case 4:
			print("Switching to your History class...\n")
			time.sleep(3)
			history()
		case 5:
			print("Switching to your Health class...\n")
			time.sleep(3)
			health()
		case -1:
			print("Now closing...")
			time.sleep(2)

mainProgram()