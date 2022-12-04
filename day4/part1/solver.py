with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

matches = 0

for line in data:
    a, b = line.split(",")
    a = a.split("-")
    a = range(int(a[0]), int(a[1]) + 1)

    b = b.split("-")
    b = range(int(b[0]), int(b[1]) + 1)

    if all([number in a for number in b]) or all([number in b for number in a]):
        matches += 1

print("Matches:", matches)