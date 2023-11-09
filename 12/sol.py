import re
from sys import stdin

def parse(moon):
    regex = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"
    res = re.match(regex, moon)
    x, y, z = res.groups()
    return [int(x), int(y), int(z)]

def gravity(moons, velocities, axis):
     for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            if moons[i][axis] < moons[j][axis]:
                velocities[j][axis] -= 1
                velocities[i][axis] += 1
            elif moons[i][axis] > moons[j][axis]:
                velocities[j][axis] += 1
                velocities[i][axis] -= 1

def velocity(moons, velocities, axis):
    for i in range(len(moons)):
        moons[i][axis] += velocities[i][axis]

def format(moons, velocities):
    res = []
    for moon, vel in zip(moons, velocities):
        pos = f"pos=<x={moon[0]: >3}, y={moon[1]: >3}, z={moon[2]: >3}>"
        vel = f"vel=<x={vel[0]: >3}, y={vel[1]: >3}, z={vel[2]: >3}>"
        res.append(f"{pos}\t{vel}")
    return "\n".join(res)

def energy(moons, velocities):
    s = 0
    for moon, vel in zip(moons, velocities):
        pot = sum(abs(x) for x in moon)
        kin = sum(abs(x) for x in vel)
        s += pot * kin
    return s

def step(moons, velocities):
    for axis in range(len(moons[0])):
        gravity(moons, velocities, axis)
        velocity(moons, velocities, axis)

def _hash(moons, velocities):
    return tuple(tuple(moon) + tuple(vel) for moon, vel in zip(moons, velocities))

def steps(moons, velocities, n):
    for i in range(n):
        step(moons, velocities)

def part1(moons):
    velocities = [[0] * len(moon) for moon in moons]
    n = 1000
    steps(moons, velocities, n)
    return energy(moons, velocities)

# clone 2d list
def clone(l):
    return [row[:] for row in l]

def get_axis(arr, axis):
    for row in arr:
        yield row[axis]

def frequency(moons, velocities, axis):
    s = set()
    steps = 0
    while (t:=tuple(get_axis(moons,axis))+tuple(get_axis(velocities,axis))) not in s:
        s.add(t)
        gravity(moons, velocities, axis)
        velocity(moons, velocities, axis)
        steps += 1
    return steps

def part2(moons):
    velocities = [[0] * len(moon) for moon in moons]
    freqs = []
    for axis in range(len(moons[0])):
        freqs.append(frequency(moons, velocities, axis))
    return lcm(*freqs)

def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)

def _lcm(a, b):
    return (a * b) // _gcd(a, b)

def lcm(*nums):
    if len(nums) == 1:
        return nums[0]
    res = _lcm(nums[0], nums[1])
    if len(nums) > 2:
        for i in range(2, len(nums)):
            res = _lcm(res, nums[i])
    return res

moons = [parse(line[:-1]) for line in stdin]

# p1
print(part1(clone(moons)))

# p2
print(part2(clone(moons)))

