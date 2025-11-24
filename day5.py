def naughtyOrNice1(strings):
    nice = 0

    for i in strings:
        status = True

        if sum(1 for j in i if j in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}) < 3:
            status = False

        if not any([i[j] == i[j+1] for j in range(len(i) - 1)]):
            status = False

        if any(j in i for j in ['ab', 'cd', 'pq', 'xy']):
            status = False

        if status:
            nice += 1

    return nice

def naughtyOrNice2(strings):
    nice = 0

    for i in strings:
        status = True

        temp = False
        for j in range(len(i)-2):
            if any([i[k]+i[k+1] == i[j:j+2] for k in range(j+2,len(i)-1)]):
                temp = True
        status = temp

        if not any([i[j] == i[j+2] for j in range(len(i) - 2)]):
            status = False

        if status:
            nice += 1

    return nice

strings = '''ugknbfddgicrmopn
aaaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
qwrtyp
abcda
xyxy
efe
zfzfz'''
strings = strings.split('\n')

print(f"Part 1: {naughtyOrNice1(strings)} \nPart 2: {naughtyOrNice2(strings)}")