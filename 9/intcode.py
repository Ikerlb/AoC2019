from collections import defaultdict

def parse(instruction):
    s=str(instruction).zfill(5);
    modes=[int(i) for i in reversed(s[:3])]
    return (int(s[3:]),modes)

def get_args(ic,modes,size,ip,base):
    args=[]
    for i in range(1,size):
        if modes[i-1]==0:
            args.append(ic[ip+i])
        elif modes[i-1]==1:
            args.append(ip+i)
        else:
            args.append(ic[ip+i]+base)
    return args


def exec(intcode,inpt):
    #instruction pointer
    ip=0
    #base for relative mode
    base=0
    #opcode size
    lengths=[0,4,4,2,2,3,3,4,4,2]
    #dict with defaults to 0
    ic=defaultdict(int)
    for k,v in enumerate(intcode):
        ic[k]=v
    opcode,modes=parse(ic[ip])
    while opcode!=99:
        args=get_args(ic,modes,lengths[opcode],ip,base)
        #updating ip here so 7 and 8 can work alright
        ip+=lengths[opcode]
        if opcode==1:
            ic[args[2]]=ic[args[0]]+ic[args[1]]
        elif opcode==2:
            ic[args[2]]=ic[args[0]]*ic[args[1]]
        elif opcode==3:
            ic[args[0]]=inpt.pop(0)
        elif opcode==4:
            yield ic[args[0]]
        elif opcode==5:
            if ic[args[0]]!=0:
                ip=ic[args[1]]
        elif opcode==6:
            if ic[args[0]]==0:
                ip=ic[args[1]]
        elif opcode==7:
            ic[args[2]]=int(ic[args[0]]<ic[args[1]])
        elif opcode==8:
            ic[args[2]]=int(ic[args[0]]==ic[args[1]])
        elif opcode==9:
            base+=ic[args[0]]
        elif opcode==99:
            break
        opcode,modes=parse(ic[ip])

