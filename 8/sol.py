image=open("input.txt","r").read()[:-1]
width=25
height=6

def repetitions(s,d):
    return len([c for c in s if c==d])
        
def least_zeros(layers):
    layer=None
    least=len(layers[0])
    for l in layers:
        r=repetitions(l,'0')
        if r<least:
            layer=l
            least=r
    return layer

def get_layers(img,w,h):
    layers=[]
    for i,p in enumerate(img):
        if i%(w*h)==0:
            layers.append([])
        layers[-1].append(p)
    return layers

def part1(img=image,w=width,h=height):
    layers=get_layers(img,w,h)
    lz=least_zeros(layers)
    print(repetitions(lz,'1')*repetitions(lz,'2'))

def part2(img=image,w=width,h=height):
    layers=get_layers(img,w,h)
    decoded=layers[0][:]
    for i in range(w*h):
        for l in layers:
            if l[i]!='2':
                decoded[i]=l[i]
                break
    return decoded

        
        
