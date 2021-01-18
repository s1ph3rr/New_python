my_string = input("Put a string>> ")
my_word = []
num = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [element]}")
        num += 1
    else:
        print(f" {num} {my_word [element] [0:11]}")
        num += 1
