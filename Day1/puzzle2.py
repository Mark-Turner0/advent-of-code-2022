f = open("input", 'r')
elves = f.read().split("\n\n")

carried = []
for elf in elves:
    all_elf = elf.splitlines()
    total_elf = sum(list(map(int, all_elf)))
    carried.append(total_elf)

carried.sort(reverse=True)
print(sum(carried[:3]))
