inputs = {}
rules = []

with open("inputs/24.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        wire, value = line.split(": ")
        value = int(value)
        inputs[wire] = value

    for line in f:
        line = line.strip()
        w1, op, w2, _, w3 = line.split()
        rules.append((w1, op, w2, w3))


while len(rules) > 0:
    for w1, op, w2, w3 in rules.copy():
        if w1 in inputs and w2 in inputs:
            match op:
                case "OR":
                    inputs[w3] = inputs[w1] | inputs[w2]
                case "AND":
                    inputs[w3] = inputs[w1] & inputs[w2]
                case "XOR":
                    inputs[w3] = inputs[w1] ^ inputs[w2]
            rules.remove((w1, op, w2, w3))

output = 0
for wire in reversed(sorted([w for w in inputs if w.startswith("z")])):
    output *= 2
    output += inputs[wire]

print(output) # 46362252142374