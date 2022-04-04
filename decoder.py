ascii_list = [131, 134, 120, 125, 122, 131, 123, 122]
swap_key = [24, 23, 12, 14, 13, 20, 15, 11]
counter_decode = 1
decoded_string = ''
print(ascii_list)
print(swap_key)
for ascii_char in ascii_list:
    decoded_letter = chr(int(ascii_char) - int(swap_key[counter_decode - 1]))
    decoded_string += decoded_letter
    counter_decode += 1
#  results
print(decoded_string)
