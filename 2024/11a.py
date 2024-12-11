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

stones = [125]

for i in range(25):
    #print(i, len(stones))
    #print(stones)
    new_stones = []
    for stone in stones:
        new_stones += step(stone)
    stones = new_stones

print(stones)
print(len(stones))