from math import prod

def splitList(lst):
    return [list(map(int, line.split("x"))) for line in lst.split('\n')]

def wrappingPaper(dimensions):
    def sides(i):
        return [i[j] * i[(j+1)%3] for j in range(3)] #lw,wh,hl
    
    return sum([ sum(sides(i))*2 + min(sides(i)) for i in dimensions ]) # 2(lw+wh+hl) + min(lw,wh,hl)

def ribbon(dimensions):
    return sum([2*min([i[j] + i[(j+1)%3] for j in range(3)]) + prod(i) for i in dimensions])

input = """2x3x4
1x1x10"""

input = splitList(input)
print(f"part1: {wrappingPaper(input)} \npart2: {ribbon(input)}")