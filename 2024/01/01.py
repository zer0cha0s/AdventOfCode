import numpy as np

# read input file
file = open("./input").read()

left = []
right = []
total = 0
p2total = 0

for line in file.splitlines():
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

# sort the lists
left = np.array(sorted(left))
right = np.array(sorted(right))


# return the difference between two numbers
def distance(a, b):
    return abs(a - b)


for a, b in zip(left, right):
    # print(distance((a), (b)))
    total = total + distance((a), (b))

print(f"Part 1: ", total)

# part 2
for c in left:
    searchval = c
    ii = np.where(right == searchval)[0]
    p2total = p2total + (len(ii) * searchval)

print(f"Part 2: ", p2total)
