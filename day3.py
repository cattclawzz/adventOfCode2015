def change(foo, by):
    if by == '>':
        foo[0] += 1
    elif by == '<':
        foo[0] -= 1
    elif by == '^':
        foo[1] += 1
    elif by == 'v':
        foo[1] -= 1

def countHouses(route):
    houses = [[0,0]]
    house = [0,0]
    for i in route:
        change(house, i)
        houses.append(house.copy())
    return len(set([tuple(i) for i in houses]))

def countHousesRobo(route):
    houses = [[0,0]]
    house = [0,0]
    houseRobo = [0,0]
    for i in range(len(route)):
        if i % 2 == 0:
            change(houseRobo, route[i])
            houses.append(houseRobo.copy())
        else:
            change(house, route[i])
            houses.append(house.copy())
    return len(set([tuple(i) for i in houses]))

route = "^>v<"
print(f"Part1: {countHouses(route)} \nPart2: {countHousesRobo(route)}")