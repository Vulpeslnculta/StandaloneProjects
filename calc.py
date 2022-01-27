def end_of_section(a, b, d):
    a = int(input("Number of last video in section:\n"))
    b = int(input("Number of video you are on now:\n"))
    d = int(input("Average length of each video in section:\n"))
    time_left = ((a-b)*d)/60
    return time_left

a = 0
b = 0
d = 0
print("Time left in this section is around {} hour(s)".format(end_of_section(a, b, d)))