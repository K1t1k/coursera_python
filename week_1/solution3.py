import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def sol_quad_equa(a, b, c):
	D = (b ** 2) - (4 * a *c)
	x1 = (- b + (D ** 0.5)) / (2 * a)
	x2 = (- b - (D ** 0.5)) / (2 * a)
	return x1, x2

sol_quad_equa(a, b, c)

print(int(sol_quad_equa(a, b, c)[0]))
print(int(sol_quad_equa(a, b, c)[1]))