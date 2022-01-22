low = 1
High = int(input("Please enter highest number of tested string: \n"))

print("Think of a number between {} and {}".format(low, High))
input("Press ENTER to start")

guess = 1
guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low, High))
    guess = low + (High - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? Enter \"h\" for higher, enter \"l\" or "
    "type \"c\" if you think my guess is correct :\n"
                     .format(guess).casefold())
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        High = guess - 1
    elif high_low == "c":
        print("You're right, I got it in {} guesses!".format(guesses))
        break
    else:
        print("ERROR: WRONG INPUT")
    # guesses = guesses + 1
    guesses += 1

