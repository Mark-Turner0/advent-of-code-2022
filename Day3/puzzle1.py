f = open("input",'r')
all_rucksacks = f.read().splitlines()
f.close()

total = 0

for rucksack in all_rucksacks:
    compA = rucksack[:len(rucksack)//2]
    compB = rucksack[len(rucksack)//2:]
    for item in compA:
        if item in compB:
            if ord(item) > ord('Z'):
                total += ord(item) % ord('a') + 1
            else:
                total += ord(item) % ord('A') + 27
            break
print(total)
