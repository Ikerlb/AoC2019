from itertools import permutations

f=open("input.txt","r").read()[:-1]
intcode=list(map(int,f.split(",")))

binop={1:lambda x,y:x+y,2:lambda x,y:x*y,7:lambda x,y:int(x<y),8:lambda x,y:int(x==y)}
unop={5:lambda x:x!=0,6:lambda x:x==0}
oplen={1:4,2:4,3:2,4:2,5:0,6:0,7:4,8:4}

def parse(i):
    lzs=str(i).zfill(5)
    return (int(lzs[3:]),lzs[2],lzs[1],lzs[0])

def param(ic,ip,m):
    if m=="0":
        return ic[ic[ip]]
    return ic[ip]

def exec(ic,inpt):
    ip=0
    (oc,m1,m2,m3)=parse(ic[ip])
    while oc!=99:
        #ic 3 means save input on next's oc address
        if oc==3:
            ic[ic[ip+1]]=inpt.pop(0)
        #return either value or address value
        elif oc==4:
            yield(param(ic,ip+1,m1))
        #unary operations
        elif oc in [5,6]:
            ip=param(ic,ip+2,m2) if unop[oc](param(ic,ip+1,m1)) else ip+3
        #binary operations
        else:
            ic[ic[ip+3]]=binop[oc](param(ic,ip+1,m1),param(ic,ip+2,m2))
        ip+=oplen[oc]
        (oc,m1,m2,m3)=parse(ic[ip])
    return

def part1(ic=intcode):
    highest=0
    for p in permutations(range(5),5):
        res=0
        inpt=list(p)
        while inpt:
            inpt.insert(1,res)
            res=next(exec(ic[:],inpt))
        if res>highest:
            highest=res
    return highest

def feedback_loop(ic,p):
    phases=[[x] for x in p]
    phases[0].append(0)
    amplifiers=[exec(ic[:],inpts) for inpts in phases]
    while True:
        for i,a in enumerate(amplifiers):
            try:
                x=next(a)
            except StopIteration:
                return x
            phases[(i+1) % len(phases)].append(x)
            
def part2(ic=intcode):
    return max(feedback_loop(ic,p) for p in permutations(range(5,10),5))


#def part2(ic=intcode):
#    highest=0
#    for p in itertools.permutations(range(5,10),5):
#        inpt=list(p)
#        inpt.insert(1,0)
#        while len(inpt)!=1:
#            gen=exec(ic[:],inpt)
#            for x in gen:
#                inpt.insert(1,x)
#                #inpt.append(x)
#                print(inpt)
#        if inpt[0]>highest:
#            highest=inpt[0]
#    return highest
            
            

