lines=open("input.txt","r").read().split("\n")[:-1]
modules=list(map(int,lines))

def part1(m=modules):
    return sum(map(lambda x:(x//3)-2,m))

def total_fuel(f):
    s=0
    while (f:=(f//3)-2)>0:
        s+=f
    return s

def part2(m=modules):
    return sum(map(total_fuel,m))

