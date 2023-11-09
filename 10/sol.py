from math import atan2,pi,inf
text=open("input.txt").read()[:-1]
height=len(text.split("\n"))
width=len(text.split("\n")[0])

def parse(s):
    asteroids=set()
    for j,line in enumerate(s.split("\n")):
        for i,c in enumerate(line):
            if c=="#":
                asteroids.add((i,j))
    return asteroids

def gcd(a,b):
    if a==0:
        return abs(b)
    if b==0:
        return abs(a)
    while (r:=a%b)!=0:
        a=b
        b=r
    return abs(b)

def detected_from(asteroids,position):
    (px,py)=position
    detected=set()
    for (ox,oy) in asteroids:
        if (px,py)==(ox,oy):
            continue
        dx=ox-px
        dy=py-oy
        d=gcd(dx,dy)
        line=(dx//d,dy//d)
        if line not in detected:
            detected.add(line)
    return detected

def angle(other):
    return atan2(other[0],other[1])%(pi*2)

def next_asteroid(asteroids,line,centre):
    i=1
    while abs(x:=(centre[0]+line[0]*i))<width and abs(y:=(centre[1]-line[1]*i))<height:
        if (t:=(x,y)) in asteroids:
            return t
        i+=1
    return None

def part1(s=text):
    asteroids=parse(s)
    r=[(position,len(detected_from(asteroids,position))) for position in asteroids]
    return max(r,key=lambda x:x[1])

def part2(s=text):
    asteroids=parse(s)
    centre,_=part1(s)
    #we want to sort raidialy with origin in centre
    detected=detected_from(asteroids,centre)
    by_angle=sorted(detected,key=lambda x:angle(x))
    i=0
    while i<200: 
        for coord in by_angle[:]: 
            if eliminated:=next_asteroid(asteroids,coord,centre):
                i+=1
            else:
                by_angle.remove(coord)
            if i==200:
                break
    return eliminated
