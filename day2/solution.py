def traversal(manual):
	horizontal, aim, depth = 0, 0, 0
	for m in manual:
		if m[0] == 'f':
			horizontal += int(m[-1])
			depth += aim*int(m[-1])
		elif m[0] == 'd':
			aim += int(m[-1])
		else:
			aim -= int(m[-1])
	return horizontal*depth
	

if __name__ == "__main__":
	with open('./input.txt') as f:
		x = f.read()
	forward = [int(y[0]) for y in x.split('forward ')[1:]]
	down = [int(y[0]) for y in x.split('down ')[1:]]
	up = [int(y[0]) for y in x.split('up ')[1:]]
	

	print("part 1", sum(forward)*(sum(down)-sum(up)))
	print("part 2", traversal(x.split('\n')[:-1]))
