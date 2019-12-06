l1,l2,_=open("input.txt","r").read().split("\n")
step={"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}

def used(w):
    s={}
    x,y,c=(0,0,0)
    for ins in w.split(","):
        d,n=ins[0],int(ins[1:])
        for _ in range(n):
            xoff,yoff=step[d]            
            x,y,c=(x+xoff,y+yoff,c+1)
            if (x,y) not in s:
                s[(x,y)]=c
    return s

def part1(w1=l1,w2=l2):
    s1=set(used(w1))
    s2=set(used(w2))
    return min([abs(x)+abs(y) for (x,y) in s1&s2])
    
def part2(w1=l1,w2=l2):
    d1=used(w1)
    d2=used(w2)
    return min([d1[p]+d2[p] for p in set(d1)&set(d2)])
