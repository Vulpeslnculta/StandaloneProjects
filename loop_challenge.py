print("_" * 80)
char = 1

while char !=0:
      print("Choose one of the following options by typing a number\n"
            "1. Learn Python\n"
            "2. Learn Java\n"
            "3. Go out\n"
            "4. Go to sleep\n"
            "0. Exit\n")
      print("_" * 80)
      char = int(input("Your choice is: \n"))
      print("_" * 80)
      if char == 1:
            print("You are learning python")
      elif char == 2:
            print("You are learning Java")
      elif char == 3:
            print("You are going out")
      elif char == 4:
            print("You are going to sleep")
      else:
            print("There is no such option as {}".format(char))
      print("_" * 80)

else:
      print("You have escaped the simulation!")
