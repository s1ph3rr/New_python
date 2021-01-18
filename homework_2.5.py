my_list = [5, 4, 3, 2, 1]
print(f"Rating - {my_list}")
digit = int(input("Insert a number>> "))
while digit != 111:
    for element in range(len(my_list)):
        if my_list[element] == digit:
            my_list.insert(element + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[element] > digit and my_list[element + 1] < digit:
            my_list.insert(element + 1, digit)
    print(f"current  list - {my_list}")
    digit = int(input("Insert a number>> "))
