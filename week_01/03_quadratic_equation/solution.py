import sys

a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

discriminant = b**2 - 4 * a * c
x1 = int((-b + discriminant**0.5) / (2 * a))
x2 = int((-b - discriminant**0.5) / (2 * a))

print(f"{x1}\n{x2}")
