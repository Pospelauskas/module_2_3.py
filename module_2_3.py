my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_list = []
index = 0
while index < len(my_list):
    if my_list[index] > 0:
        positive_list.append(my_list[index])
    elif my_list[index] < 0:
        break
    index += 1
print(positive_list)


