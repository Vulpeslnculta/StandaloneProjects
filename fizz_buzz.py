MAX = 100
MIN = 1


def fizz_buzz(min: int, max: int):
    """
    Classical Fizz-Buzz game in form of function.
    :param min: That's a starting value
    :param max: That's an end value
    :return: Strings where numbers are tagged with
    "fizz" for those divisible by 3, "buzz" for those divisible by 5,
    and "fizz buzz" for numbers with both given properties.
    """
    for number in range(min, max + 1):
        if number % 3 == 0:
            if number % 5 == 0:
                print("{}: fizz buzz".format(number))
            else:
                print("{}: fizz".format(number))
        elif number % 5 == 0:
            print("{}: buzz".format(number))
        else:
            print(number)




print(fizz_buzz(MIN, MAX))