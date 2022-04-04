import random

input_string = input("Input data to encode:\n")
ascii_list = []
decoded_string = ''
swap_key = []
counter_encode = 1
counter_decode = 1

#  encoder
for letter in input_string:
    swap_key.append(random.randint(1, 25))
    ascii_letter = ord(letter)
    ascii_letter += swap_key[counter_encode - 1]
    ascii_list.append(ascii_letter)
    counter_encode += 1

#  output
print("Your data is encrypted: " + str(ascii_list))
print("Save that Key to decode your data later!!!: " + str(swap_key))
