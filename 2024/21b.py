from functools import cache
from itertools import permutations
import numpy as np

with open("inputs/21.txt") as f:
    codes = f.readlines()
    codes = [code.strip() for code in codes]

numpad = np.array(
    [
        [ "7", "8", "9" ],
        [ "4", "5", "6" ],
        [ "1", "2", "3" ],
        [ " ", "0", "A" ],
    ]
)

dirpad = np.array(
    [
        [ " ", "^", "A" ],
        [ "<", "v", ">" ]
    ]
)

dirpad_moves = {}
for sx, sy in np.ndindex(dirpad.shape):
    start_char = dirpad[sx, sy]
    for ex, ey in np.ndindex(dirpad.shape):
        end_char = dirpad[ex, ey]
        dx = ex-sx # positive= "v", negative= "^"
        dy = ey-sy # positive= ">", negative= "<"
        if dx >= 0:
            if dy >= 0:
                moves = "v" * dx + ">" * dy
            else:
                moves = "<" * -dy + "v" * dx
        else:
            if dy >= 0:
                moves = "^" * -dx + ">" * dy
            else:
                moves = "<" * -dy + "^" * -dx
        dirpad_moves[start_char + end_char] = moves + "A"
# Special cases to avoid empty slot:
dirpad_moves["A<"] = "v<<A"
dirpad_moves["^<"] = "v<A"
dirpad_moves["<^"] = ">^A"
dirpad_moves["<A"] = ">>^A"

numpad_moves = {}
for sx, sy in np.ndindex(numpad.shape):
    start_char = numpad[sx, sy]
    for ex, ey in np.ndindex(numpad.shape):
        end_char = numpad[ex, ey]
        dx = ex-sx # positive= "v", negative= "^"
        dy = ey-sy # positive= ">", negative= "<"
        if dx >= 0:
            if dy >= 0:
                moves = "v" * dx + ">" * dy
            else:
                moves = "<" * -dy + "v" * dx
        else:
            if dy >= 0:
                moves = "^" * -dx + ">" * dy
            else:
                moves = "<" * -dy + "^" * -dx
        numpad_moves[start_char + end_char] = moves + "A"
# Special cases to avoid empty slot:
numpad_moves["A1"] = "^<<A"
numpad_moves["A4"] = "^^<<A"
numpad_moves["A7"] = "^^^<<A"
numpad_moves["01"] = "^<A"
numpad_moves["04"] = "^^<A"
numpad_moves["07"] = "^^^<A"
numpad_moves["10"] = ">vA"
numpad_moves["1A"] = ">>vA"
numpad_moves["40"] = ">vvA"
numpad_moves["4A"] = ">>vvA"
numpad_moves["70"] = ">vvvA"
numpad_moves["7A"] = ">>vvvA"
    
def numpad_move(code):
    moves = ""
    last = "A"
    for c in code:
        moves += numpad_moves[last + c]
        last = c
    return moves

@cache
def dirpad_move_length(code, depth=0):
    move_length = 0
    last = "A"
    for c in code:
        if depth == 0:
            move_length += len(dirpad_moves[last + c])
        else:
            move_length += dirpad_move_length(dirpad_moves[last + c], depth-1)
        last = c
    return move_length

num_robots = 25

complexity = 0
for code in codes:
    moves = numpad_move(code)
    move_length = dirpad_move_length(moves, depth=num_robots-1)
    complexity += int(code[:-1]) * move_length
    print(code, move_length, complexity)

print(complexity)
