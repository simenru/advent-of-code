inputs = {}
rules = []

with open("inputs/24.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break

    for line in f:
        line = line.strip()
        w1, op, w2, _, w3 = line.split()
        rules.append((w1, op, w2, w3))

def swap(w1, w2, rules: list):
    for rule in rules:
        _, _, _, w = rule
        if w == w1:
            w1_rule = rule
        if w == w2:
            w2_rule = rule
    
    r = rules.copy()
    r.remove(w1_rule)
    r.remove(w2_rule)
    w11, op1, w12, _ = w1_rule
    w21, op2, w22, _ = w2_rule
    r.append((w11, op1, w12, w2))
    r.append((w21, op2, w22, w1))
    return r

x = ["" for _ in range(44)]
y = ["" for _ in range(44)]
a = ["" for _ in range(44)]
b = ["" for _ in range(44)]
c = ["" for _ in range(44)]
d = ["" for _ in range(44)]
z = ["" for _ in range(44)]

rules = swap("z06", "jmq", rules)
rules = swap("z13", "gmh", rules)
rules = swap("cbd", "rqf", rules)
rules = swap("qrh", "z38", rules)
#print(rules)

for i in range(44):
    x[i] = f"x{i:02d}"
    y[i] = f"y{i:02d}"
    for w1, op, w2, w3 in rules:
        if (w1 == x[i] or w2 == x[i]) and op == "XOR":
            # w3 should be a_i
            a[i] = w3
        if (w1 == x[i] or w2 == x[i]) and op == "AND":
            # w3 should be b_i
            b[i] = w3
    
    for w1, op, w2, w3 in rules:
        if (w1 == a[i] or w2 == a[i]) and op == "XOR":
            z[i] = w3
        if (w1 == a[i] or w2 == a[i]) and op == "AND":
            d[i] = w3
        if (w1 == b[i] or w2 == b[i]) and op == "OR":
            c[i] = w3

#print(x[6], y[6], z[6], a[6], b[6], c[6], d[6])
print(z)


print(",".join(sorted(["z06", "jmq", "z13", "gmh", "cbd", "rqf", "qrh", "z38"])))


exit()
def calculate(x: int, y: int, rules) -> int:
    inputs = {}
    for i in range(45):
        inputs[f"x{i:02d}"] = x % 2
        inputs[f"y{i:02d}"] = y % 2
        x = x // 2
        y = y // 2
    
    rules = rules.copy()
    last_length = len(rules)
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
        if len(rules) == last_length:
            return -1
        last_length = len(rules)

    output = 0
    for wire in reversed(sorted([w for w in inputs if w.startswith("z")])):
        output *= 2
        output += inputs[wire]
    
    return output



def test_rules(rules, p=False):
    for i in range(2**25):
        for j in range(2**25):
            if calculate(i, j, rules.copy()) != i + j:
                if p: print(i, j)
                return False
    return True




rules = swap("z06", "jmq", rules)
rules = swap("z13", "gmh", rules)

#print(calculate(0, 8192, rules))
test_rules(rules, p=True)

exit()
for rule in rules:
    _, _, _, w3 = rule
    print(w3)
    if w3 == "z13": continue
    r = swap("z13", w3, rules)
    if test_rules(r, p=True):
        print("----", w3)

# z06, jmq should be swapped
# z13