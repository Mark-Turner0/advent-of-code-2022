f = open("input", 'r')
pairs = f.read().splitlines()
f.close()
overlap = 0

for pair in pairs:
    pair = pair.split(',')
    start1, start2 = pair[0].split('-')
    end1, end2 = pair[1].split('-')
    first_elf = list(range(int(start1), int(start2) + 1))
    second_elf = list(range(int(end1), int(end2) + 1))
    elves = first_elf + second_elf
    if len(elves) != len(set(elves)):
        overlap += 1

print(overlap)
