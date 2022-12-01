f = open("input", 'r')
elves = f.read().split("\n\n")

highest = 0
for elf in elves:
    all_elf = elf.splitlines()
    total_elf = sum(list(map(int, all_elf)))
    if total_elf > highest:
        highest = total_elf

print(highest)
