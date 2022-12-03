f = open("input", 'r')
rounds = f.read().splitlines()
f.close()
score = 0

for line in rounds:
    line = line.split()
    opp_choice = ord(line[0]) % ord('A')
    match line[1]:
        case 'Z':
            your_choice = (opp_choice + 1) % 3
            score += your_choice + 1 + 6
        case 'X':
            your_choice = (opp_choice - 1) % 3
            score += your_choice + 1
        case 'Y':
            score += opp_choice + 1 + 3

print(score)
