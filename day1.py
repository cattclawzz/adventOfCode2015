def findFloor(floor, instructions):
    for i in instructions:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
    return(floor)

print(findFloor(0, input()))