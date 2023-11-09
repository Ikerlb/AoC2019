import intcode

text=open("input.txt").read()[:-1].split(",")
ic=list(map(int,text))

def part1(prog=ic):
    for r in intcode.exec(prog,[1]):
        print(r)

def part2(prog=ic):
    for r in intcode.exec(prog,[2]):
        print(r)
        
