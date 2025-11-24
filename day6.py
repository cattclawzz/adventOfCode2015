lights = [[False for j in range(1000)] for i in range(1000)]
lights2 = [[0 for j in range(1000)] for i in range(1000)]

input = '''toggle 461,550 through 564,900
turn off 370,39 through 425,839
turn off 464,858 through 833,915
turn off 812,389 through 865,874
turn on 599,989 through 806,993'''
lst = [i.split(' ') for i in input.split('\n')]

for i in lst:
    if i[0] == 'turn':
        i.pop(0)
    i.pop(2)
    for k in range(1,3):
        i[k] = [int(j) for j in i[k].split(",")]

def change(action, xy1, xy2, lst):
    for x in range(xy1[0], xy2[0]+1):
        for y in range(xy1[1], xy2[1]+1):
            if action == 'on':
                lst[x][y] = True
            elif action == 'off':
                lst[x][y] = False
            elif action == 'toggle':
                lst[x][y] = not lst[x][y]
    return lst

def change2(action, xy1, xy2, lst):
    for x in range(xy1[0], xy2[0]+1):
        for y in range(xy1[1], xy2[1]+1):
            if action == 'on':
                lst[x][y] += 1
            elif action == 'off' and lst[x][y] > 0:
                lst[x][y] -=1
            elif action == 'toggle':
                lst[x][y] += 2
    return lst

for i in lst:
    change(i[0], i[1], i[2], lights)
    change2(i[0], i[1], i[2], lights2)

print(f"Part1: {sum([sum(i) for i in lights])} \nPart2: {sum([sum(i) for i in lights2])}")