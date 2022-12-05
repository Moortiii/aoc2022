from collections import defaultdict

with open("input.txt") as f:
    data = f.readlines()
    boxes = [line for line in data if "1" not in line]
    boxes = [line for line in data if "move" not in line]
    boxes = [line[1::4] for line in boxes]

    moves = data[len(boxes):]
    moves = [line.strip() for line in moves]
    moves = [line.split(" ") for line in moves]
    moves = [(int(line[1]), int(line[3]), int(line[5])) for line in moves]

    boxes = boxes[:-2]

box_mapping = defaultdict(list)

for line in boxes:
    for i, char in enumerate(line):
        if char != " ":
            box_mapping[i].append(char)

for line in moves:
    a,b,c = line
    
    crates = []

    for i in range(a):
        crates.append(box_mapping[b - 1].pop(0))

    for crate in crates[::-1]:
        box_mapping[c - 1].insert(0, crate)

output = "".join(v[0] for k,v in sorted(box_mapping.items()))
print("Boxes:", output)
