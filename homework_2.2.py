uwu_count = int(input("Put a list elements number>> "))
my_list = []
a = 0
w = 0
while a < uwu_count:
    my_list.append(input("Put next list elements number>> "))
    a += 1

for element in range(int(len(my_list)/2)):
        my_list[w], my_list[w + 1] = my_list [w + 1], my_list[w]
        w += 2
print(my_list)
