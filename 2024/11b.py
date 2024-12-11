with open("inputs/11.txt") as input:
    stones = input.readline()
    stones = stones.strip()
    stones = stones.split()
    stones = [int(s) for s in stones]

def step(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]
    else:
        return [stone * 2024]

step5: dict[int, list[int]] = {}
def five_steps(stone: int) -> list[int]:
    if stone in step5:
        return step5[stone]

    stones = [stone]
    for i in range(5):
        new_stones = []
        for s in stones:
            new_stones += step(s)
        stones = new_stones
    step5[stone] = stones
    return stones

step25: dict[int, list[int]] = {}
def twentyfive_steps(stone: int) -> list[int]:
    if stone in step25:
        return step25[stone]
    
    stones = [stone]
    for i in range(5):
        new_stones = []
        for s in stones:
            new_stones += five_steps(s)
        stones = new_stones
    step25[stone] = stones
    return stones

l50: dict[int, int] = {}
def length50(stone: int) -> int:
    if stone in l50:
        return l50[stone]

    s25 = twentyfive_steps(stone)
    l = 0
    for s in s25:
        l += len(twentyfive_steps(s))
    l50[stone] = l
    return l


l = 0
for stone in stones:
    s25 = twentyfive_steps(stone)
    print(f"{stone=}, {len(s25)=}")
    for s in s25:
        l += length50(s)

print(l)