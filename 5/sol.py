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
		if oc==3:
			ic[ic[ip+1]]=inpt
		elif oc==4:
			yield(param(ic,ip+1,m1))
		elif oc in [5,6]:
			ip=param(ic,ip+2,m2) if unop[oc](param(ic,ip+1,m1)) else ip+3
		else:
			ic[ic[ip+3]]=binop[oc](param(ic,ip+1,m1),param(ic,ip+2,m2))
		ip+=oplen[oc]		
		(oc,m1,m2,m3)=parse(ic[ip])
	
def part1(ic=intcode[:]):
	for i in exec(ic,1):
		if i!=0:
			return i

def part2(ic=intcode[:]):
	for i in exec(ic,5):
		if i!=0:
			return i
