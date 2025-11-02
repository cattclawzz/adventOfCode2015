def findFloor(floor, instructions):
    basement = 0
    for char in range(len(instructions)):
        if instructions[char] == '(':
            floor += 1
        elif instructions[char] == ')':
            floor -= 1
        if floor < 0 and basement == 0:
            basement = char + 1

    return(f"Part 1: {floor} \nPart 2: {basement}")

print(findFloor(0, input()))