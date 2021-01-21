import sys

steps_num = int(sys.argv[1])

for i in range(1, steps_num + 1):
    spaces = " " * (steps_num - i)
    stair = "#" * i
    print(f"{spaces}{stair}")
