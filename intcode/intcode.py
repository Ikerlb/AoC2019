from collections import defaultdict, deque

def parse(instruction):
    s = str(instruction).zfill(5);
    modes = [int(i) for i in reversed(s[:3])]
    return (int(s[3:]), modes)

def get_args(ic, modes, size, ip, base):
    args = []
    for i in range(1, size):
        if modes[i - 1] == 0:
            args.append(ic[ip + i])
        elif modes[i - 1] == 1:
            args.append(ip + i)
        else:
            args.append(ic[ip + i] + base)
    return args

class InputInterrupt(Exception):
    pass

class Intcode:
    # opcode size
    lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

    def __init__(self, intcode, inpt):
        self.intcode = intcode
        self.inpt = inpt
        self.done = False
        # instruction pointer
        self.ip = 0
        # base for relative mode
        self.base = 0
        # dict with defaults to 0
        self.ic = defaultdict(int)
        for k, v in enumerate(intcode):
            self.ic[k] = v

    def exec(self):
        opcode, modes = parse(self.ic[self.ip])
        while opcode != 99:
            args = get_args(self.ic, modes, self.lengths[opcode], self.ip, self.base)
            #updating ip here so 7 and 8 can work alright??
            #self.ip += self.lengths[opcode]
            if opcode == 1:
                self.ip += 4
                self.ic[args[2]] = self.ic[args[0]] + self.ic[args[1]]
            elif opcode == 2:
                self.ip += 4
                self.ic[args[2]] = self.ic[args[0]] * self.ic[args[1]]
            elif opcode == 3:
                if len(self.inpt) == 0:
                    raise InputInterrupt
                self.ic[args[0]] = self.inpt.popleft()
                self.ip += 2
            elif opcode == 4:
                self.ip += 2
                yield self.ic[args[0]]
            elif opcode == 5:
                self.ip += 3
                if self.ic[args[0]] != 0:
                    self.ip = self.ic[args[1]]
            elif opcode == 6:
                self.ip += 3
                if self.ic[args[0]] == 0:
                    self.ip = self.ic[args[1]]
            elif opcode == 7:
                self.ip += 4
                self.ic[args[2]] = int(self.ic[args[0]] < self.ic[args[1]])
            elif opcode == 8:
                self.ip += 4
                self.ic[args[2]] = int(self.ic[args[0]] == self.ic[args[1]])
            elif opcode == 9:
                self.ip += 2
                self.base += self.ic[args[0]]
            elif opcode == 99:
                break
            opcode, modes = parse(self.ic[self.ip])
        self.done = True
