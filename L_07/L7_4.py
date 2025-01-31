def common_elements():
	num_set = set()
	for i in range(0, 100):
		if (i % 3) == 0 and (i % 5) == 0:
			num_set.add(i)
	return num_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}