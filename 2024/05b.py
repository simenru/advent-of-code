from dataclasses import dataclass

with open("./inputs/05.txt") as input:
    rules = []
    manuals = []

    for line in input:
        line = line.strip()
        if line == "":
            break
        rules.append(line)
    
    for line in input:
        line = line.strip()
        manuals.append(line)

following = {}
for rule in rules:
    first, second = rule.split("|")
    first, second = int(first), int(second)
    if not first in following:
        following[first] = {second}
    else:
        following[first].add(second)

@dataclass
class page():
    pagenum: int

    def __lt__(self, other):
        if not self.pagenum in following:
            return True
        if other.pagenum in following[self.pagenum]: 
            return True
        return False

sum = 0

for manual in manuals:
    pages = [page(int(m)) for m in manual.split(",")]
    if not all(pages[i] < pages[i+1] for i in range(len(pages)-1)):
        pages = sorted(pages)
        sum += pages[len(pages)//2].pagenum

print(sum)
