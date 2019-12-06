sr=range(356262,846303)

def non_decreasing(n):
	prev=int(str(n)[0])
	for c in str(n)[1:]:
		if int(c)<prev:
			return False
		prev=int(c)
	return True

def to_dict(n):
	d={}
	for c in str(n):
		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	return d

def part1(r=sr):
	nd=[i for i in r if non_decreasing(i)]
	l=[i for i in nd if max(to_dict(i).values())>1]
	return len(l)

def part2(r=sr):
	nd=[i for i in r if non_decreasing(i)]
	l=[i for i in nd if 2 in to_dict(i).values()]
	return len(l)
