available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "Microphone",
                   "DVD drive",
                   "Gaming Chair"
                   ]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)
current_basket = "-"
computer_parts = []  # empty list
add_item = []
while current_basket != '0':
    if current_basket in valid_choices:
        index = int(current_basket) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing part no. {}".format(current_basket))
            computer_parts.remove(chosen_part)
        else:
            print("Adding part no. {}".format(current_basket))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    elif current_basket == '515':
        add_item = input("Please add new item to the shop:\n")
        available_parts.append(add_item)
        valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
        print(valid_choices)
    else:
        print("Add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{}: {}".format(number + 1, part))
    current_basket = input()
print(valid_choices)
print(computer_parts)