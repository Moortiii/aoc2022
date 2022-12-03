from string import ascii_lowercase

with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

priorities = []

for line in data:
    rucksack_1 = line[:len(line) // 2]
    rucksack_2 = line[len(line) // 2:]

    intersection = list(set(rucksack_1).intersection(set(rucksack_2))).pop()
    
    if intersection in ascii_lowercase:
        priorities.append(ord(intersection) - 96)
    else:
        priorities.append(ord(intersection.lower()) - 96 + 26)

print("Sum:", sum(priorities))