from collections import defaultdict
from functools import cache

connections = defaultdict(set)

with open("inputs/23.txt") as f:
    for line in f:
        line = line.strip()
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)

lans = set()
def bron_kerbosch1(r: set[str], p: set[str], x: set[str]):
    global lans
    if len(p) == 0 and len(x) == 0:
        lans.add(tuple(sorted(r)))
    for v in p.copy():
        bron_kerbosch1(r.union({v}), p.intersection(connections[v]), x.intersection(connections[v]))
        p.discard(v)
        x.add(v)

bron_kerbosch1(set(), set(connections), set())

largest_lan = tuple()
for lan in lans:
    if len(lan) > len(largest_lan):
        largest_lan = lan
print(",".join(largest_lan))