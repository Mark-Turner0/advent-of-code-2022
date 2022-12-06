f = open("input", 'r')
pairs = f.read().splitlines()
f.close()
fully_contains = 0

for pair in pairs:
    pair = pair.split(',')
    start1, start2 = pair[0].split('-')
    end1, end2 = pair[1].split('-')
    first_elf = list(range(int(start1), int(start2)+1))
    second_elf = list(range(int(end1), int(end2)+1))
    elves = first_elf + second_elf
    difference = len(elves) - len(set(elves))
    if difference == len(first_elf) or difference == len(second_elf):
        fully_contains += 1

print(fully_contains)
