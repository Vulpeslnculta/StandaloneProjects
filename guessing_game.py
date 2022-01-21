from random import randint

answer = randint(0, 10)

print("Please guess the number between 1 and 10: \n")
guess = int(input())

if guess == answer:
    print("Dang it! You're right!")
elif guess > answer:
    print("Your guess was too high, correct answer is {0}. And remember, House always wins!".format(answer))
else:
    print("Your guess was too low, correct answer is {0}. And remember, House always wins!".format(answer))