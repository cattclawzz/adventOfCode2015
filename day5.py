def naughtyOrNice(strings):
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

strings = '''ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
qwrtyp
abcda'''
strings = strings.split('\n')

print(naughtyOrNice(strings))