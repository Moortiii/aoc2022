from string import ascii_lowercase

with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

groups = []
group = []

for i, line in enumerate(data):
    if i % 3 == 0 and i != 0:
        groups.append(group)
        group = []

    group.append(set(line))

groups.append(group)

priorities = []

for group in groups:
    a, b, c = group

    intersection = list(a.intersection(b).intersection(c)).pop()

    if intersection in ascii_lowercase:
        priorities.append(ord(intersection) - 96)
    else:
        priorities.append(ord(intersection.lower()) - 96 + 26)

print("Sum:", sum(priorities))