f=open("input.txt","r").read()[:-1]
orbits=f.split("\n")

def construct(l):
    d={}
    for s in l:
        p,o=s.split(")")
        if p not in d:
            d[p]=[]
        d[p].append(o)
    return d

def rec(d,node,depth):
    if node in d:
        s=0
        for c in d[node]:
            s+=rec(d,c,depth+1)
        return s+depth
    return depth

def path_to(d,node,to,l):
    if node==to:
        return l
    if node in d:
        res=[]
        for c in d[node]:
            res+=path_to(d,c,to,l+[node])
        return res
    return []


def part1(o=orbits):
    d=construct(o)
    return rec(d,"COM",0)

def part2(o=orbits):
    d=construct(o)
    a=set(path_to(d,'COM','YOU',[]))
    b=set(path_to(d,'COM','SAN',[]))
    return len(a-b)+len(b-a)
