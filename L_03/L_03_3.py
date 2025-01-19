list = [1, 2, 3, 4, 5, 6]# => [[1, 2, 3], [4, 5, 6]]
#list = [1, 2, 3]# => [[1, 2], [3]]
#list = [1, 2, 3, 4, 5]# => [[1, 2, 3], [4, 5]]
#list = [1]# => [[1], []]
#list = []# => [[], []]

if (len(list) % 2) == 0:
    length_1 = len(list)/2
    length_2 = length_1
else:
    length_2 = len(list) // 2
    length_1 = length_2 + 1

list_1 = list[:int(length_1)]
list_2 = list[int(length_1):int(len(list))]

new_list = []
new_list.append(list_1)
new_list.append(list_2)

print(new_list)