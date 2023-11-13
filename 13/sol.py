import sys
import os
sys.path.append('../intcode')
from intcode import Intcode, InputInterrupt
from math import inf
from itertools import batched, islice
from collections import deque
import time

code = [int(n) for n in input().split(",")]

def format(grid):
    mxr = mxc = -inf
    for row, col in grid:
        mxr = max(mxr, row)
        mxc = max(mxc, col)

    res = []
    score = grid.get((0, -1), 0)
    for r in range(0, mxr + 1):
        row = []
        for c in range(0, mxc + 1):
            row.append(grid[(r, c)])
        res.append("".join(row)) 

    return f"{score}\n" + "\n".join(res)

def play(code, inpt, debug = False):
    grid = {}
    intcode = Intcode(code, inpt)
    res = []
    ballc = score = dashc = None
    while not intcode.done:
        try:
            out = next(intcode.exec())
            res.append(out)
            if len(res) == 3:
                col, row, tile_id = res
                if (row, col) == (0, -1):
                    score = tile_id
                elif tile_id == 0:
                    grid[(row, col)] = " "
                elif tile_id == 1:
                    grid[(row, col)] = "|"
                elif tile_id == 2:
                    grid[(row, col)] = "#"
                elif tile_id == 3:
                    dashc = col
                    grid[(row, col)] = "-"
                elif tile_id == 4:
                    ballc = col
                    grid[(row, col)] = "o"
                res.clear()
        except InputInterrupt:
            if debug:
                time.sleep(0.05)
                os.system("clear")
                print(format(grid))
            if ballc < dashc:
                inpt.append(-1)
            elif ballc > dashc:
                inpt.append(1)
            else:
                inpt.append(0)
            #break
        except StopIteration:
            break
        except KeyboardInterrupt:
            return grid, score
    return grid, score

def part1(code):
    grid, _ = play(code, deque([]))
    return sum(1 for v in grid.values() if v == "#")

def part2(code):
    code[0] = 2
    _, score = play(code, deque([]))
    return score

print(part1(code[:]))
print(part2(code[:]))
