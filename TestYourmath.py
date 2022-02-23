#!/usr/bin/python3

import random, time, os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + color.YELLOW + "\n Note: This code is written by Rahul Choudhari, a proud father of her daughter named  Aashrita\n" + color.END)
STUD = input("\nPlease enter your name: " + color.CYAN + "")
MATHTYPE = input(color.END + color.BOLD + "\nWhat you want to do:\n1) Addition\n2) Subtraction\nEnter your choice: (\"1\" or \"2\"): ")
CHOICE = input("\n" + color.END + "Please select your challenge mode:\n1) Simple\n2) Medium\n3) Hard\nEnter your choice: (\"1\" or \"2\" or \"3\"): ")
print(color.BOLD + color.PURPLE +"\nYour challenge is starting now, all the best !!!\n" + color.END)

CHL = 1
CORRECT = 0
FALSE = 0
DEC = "Continue"
MAXCHL = 20

# Condition to run logic
while DEC != "Exit":
  # Defining varaibles for addition
  IntA = ""
  IntB = ""
  if int(CHOICE) == 1:
      IntA = random.randint(1,10)
      IntB = random.randint(0,10)
  elif int(CHOICE) == 2:
      IntA = random.randint(10,100)
      IntB = random.randint(0,10)
  elif int(CHOICE) == 3:
      IntA = random.randint(10,100)
      IntB = random.randint(0,99)
  else:
      IntA = random.randint(1,10)
      IntB = random.randint(0,10)
  print("++++++++++++++++++++++++++++++++++++++++++++++++++\n")
  print("Challenge:" + str(CHL) + "\n")
#  Ans = input("Please add number " + color.CYAN + str(IntA) + color.END + " + " + color.CYAN + str(IntB) + color.END + " ==> ")
  if int(MATHTYPE) == 1:
    OUT = IntA + IntB
    Ans = input("Please add number " + color.CYAN + str(IntA) + color.END + " + " + color.CYAN + str(IntB) + color.END + " ==> ")
  if int(MATHTYPE) == 2:
    OUT = max(IntA,IntB) - min(IntA,IntB)
    Ans = input("Please subtract number " + color.CYAN + str(max(IntA,IntB)) + color.END + " - " + color.CYAN + str(min(IntA,IntB)) + color.END + " ==> ")
  if str(OUT) == str(Ans):
      print(color.BOLD + color.GREEN + "\nYour answer is correct, Great Job!!!\n" + color.END)
      CORRECT = CORRECT + 1
  else:
      print(color.BOLD + color.RED +"\nYou are wrong, the correct answer is " + color.BOLD + color.GREEN + str(OUT) + color.END + ". Better luck next challenge :-( \n" + color.END)
      FALSE = FALSE + 1

  print(color.BOLD + color.CYAN + STUD + color.END + " so far you answered " + color.BOLD + color.GREEN + str(CORRECT)  + color.END + " correct and " + color.BOLD + color.RED + str(FALSE) + color.END + " wrong")

  CHL = CHL + 1
  time.sleep(5)
  os.system('cls||clear')
  if int(CHL) > int(MAXCHL):
      DEC = input("\n" + color.PURPLE + "CONGRATULATIONS !!! " + color.END + " your test is complete, you have answered " + color.BOLD + color.GREEN + str(CORRECT) + color.END + " correct out of " + str(MAXCHL) + " questions. If you want to continue with more challenges, please type " + color.GREEN + "\"More\"" + color.END + "  or type " + color.RED + "\"Exit\"" + color.END + " for exiting this challenge: ")
      MAXCHL = MAXCHL + 10
