f=open("input.txt","r").read()[:-1]
intcode=list(map(int,f.split(",")))

ops={1:lambda x,y:x+y,2:lambda x,y:x*y}

def exec(ic,noun,verb):
	ic[1]=noun
	ic[2]=verb
	cur=0
	while (oc:=ic[cur])!=99:
		ic[ic[cur+3]]=ops[oc](ic[ic[cur+1]],ic[ic[cur+2]])
		cur+=4
	return ic

def part1(ic=intcode):
	return exec(ic[:],12,2)[0]

def part2(ic=intcode):
	for noun in range(100):
		for verb in range(100):
			if exec(ic[:],noun,verb)[0]==19690720:
				return noun,verb
