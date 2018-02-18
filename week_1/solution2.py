import sys

num_step = int(sys.argv[1])

for step in range(1, num_step + 1):
	print(" " * (num_step - step) + "#" * step)