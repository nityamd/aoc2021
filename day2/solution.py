if __name__ == "__main__":
	with open('./input.txt') as f:
		x = f.read()
	forward = [int(y[0]) for y in x.split('forward ')[1:]]
	down = [int(y[0]) for y in x.split('down ')[1:]]
	up = [int(y[0]) for y in x.split('up ')[1:]]

	print("part 1", sum(forward)*(sum(down)-sum(up)))
