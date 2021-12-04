def answer(array):
	count = 0
	for i in range(1,len(array)):
		if array[i] > array[i-1]:
			count +=1
	return count

if __name__ == "__main__":
	with open('input.txt') as f:
        	_input = f.read()
	x = list(map(int, _input.split('\n')[:-1]))
	print("part1", answer(x))

	window_sum_array = []
	for i in range(1, len(x)-1):
		window_sum_array.append(x[i-1] + x[i] + x[i+1])

	print("part2", answer(window_sum_array))

