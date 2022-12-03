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

print(sum(sorted([sum(elf) for elf in elves])[::-1][:3]))
