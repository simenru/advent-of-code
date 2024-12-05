from dataclasses import dataclass

after: dict[int, set[int]] = {}
manuals: list[list[int]] = []

with open("./inputs/05.txt") as input:
    rules = []
    manuals = []

    for line in input:
        line = line.strip()
        if line == "":
            # Move on to specifying manuals
            break
        first, second = line.split("|")
        first, second = int(first), int(second)
        if not first in after:
            after[first] = {second}
        else:
            after[first].add(second)
    
    for line in input:
        line = line.strip()
        manuals.append(map(int, line.split(",")))

@dataclass
class page():
    pagenum: int

    def __lt__(self, other):
        if not self.pagenum in after:
            return True
        if other.pagenum in after[self.pagenum]: 
            return True
        return False

sum = 0

for manual in manuals:
    pages = [page(p) for p in manual]
    if not all(pages[i] < pages[i+1] for i in range(len(pages)-1)):
        pages = sorted(pages)
        sum += pages[len(pages)//2].pagenum

print(sum)
