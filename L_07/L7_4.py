def common_elements():
	lst_1 = []
	lst_2 = []

	for i in range(0, 100):
		if (i % 3) == 0:
			lst_1.append(i)
		if (i % 5) == 0:
			lst_2.append(i)

	num_set_1 = set(lst_1)
	num_set_2 = set(lst_2)
	num_set_1.intersection_update(num_set_2)
	return num_set_1

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}