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

#  debugger
print(ascii_list)
print(swap_key)

#  decoder
for ascii_char in ascii_list:
    decoded_letter = chr(ascii_char - swap_key[counter_decode - 1])
    decoded_string += decoded_letter
    counter_decode += 1
#  results
print(decoded_string)
