f = open("input",'r')
all_rucksacks = f.read().splitlines()
f.close()

total = 0
index = 0

while (index < len(all_rucksacks)):
    rucksack_A = all_rucksacks[index]
    rucksack_B = all_rucksacks[index + 1]
    rucksack_C = all_rucksacks[index + 2]
    for item in rucksack_A:
        if item in rucksack_B and item in rucksack_C:
            if ord(item) > ord('Z'):
                total += ord(item) % ord('a') + 1
            else:
                total += ord(item) % ord('A') + 27
            break
    index += 3

print(total)
