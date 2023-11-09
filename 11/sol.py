from intcode import exec
from collections import defaultdict
from math import cos,sin,pi

text=open("input.txt").read()[:-1]
prog=list(map(int,text.split(",")))

turn=[(pi/2),-(pi/2)]

def rotate(rads):
    return (int(cos(rads)),int(sin(rads)))

def simulation(ic=prog,init_panel=0):
    panels=defaultdict(int)
    position=(0,0)
    direction=pi/2
    inputs=[init_panel]

    gen=exec(ic[:],inputs)
    while True:
        try:
            panels[position]=next(gen)
            new_dir=next(gen)
            adv=rotate(direction:=(direction+turn[new_dir]))
            position=(position[0]+adv[0],position[1]+adv[1])
            inputs.append(panels[position])
        except StopIteration:
            break
    return panels

def part2(ic=prog):
    #get width and height
    panels=simulation(ic,1)
    minw=min(panel[0] for panel in panels)
    maxw=max(panel[0] for panel in panels)
    minh=min(panel[1] for panel in panels)
    maxh=max(panel[1] for panel in panels)
    for j in range(minh,maxh+1):
        row=[]
        for i in range(minw,maxw+1):
            if panels[(i,j)]==1:
                row.append("#")
            else:
                row.append(" ")
        print("".join(row))
