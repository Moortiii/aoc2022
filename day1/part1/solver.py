with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]


elves = []

elf = []

for line in data:
    if line == "":
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

highest = 0

for i, elf in enumerate(elves):
    if sum(elf) > highest:
        highest = sum(elf)
        highest_index = i

print(highest)
