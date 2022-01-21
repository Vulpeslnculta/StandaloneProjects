import random
highest = int(input("Please input highest number of string:\n")) + 1
check = 0
number = random.randint(1, highest)
answer = int(input("Make your guess: \n"))
print("_" * 30)
while answer != number:
    if answer == 0:
        check += 1
        print("Are you afraid? That's why you quit I guess")
        break
    elif answer < number:
        print("Guess higher next time!")
        answer = int(input("Try again!\n"))
        print("_" * 30)
    elif answer > number:
        print("Guess lower next time!")
        answer = int(input("Try again!\n"))
        print("_" * 30)
    else:
        break
if check == 0:
    print("You got it!")

