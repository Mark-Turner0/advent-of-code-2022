f = open("input", 'r')
rounds = f.read().splitlines()
f.close()
score = 0

for line in rounds:
    line = line.split()
    opp_choice = ord(line[0]) % ord('A')
    your_choice = ord(line[1]) % ord('X')
    if (your_choice == (opp_choice + 1) % 3):
        score += your_choice + 1 + 6
    elif (your_choice == (opp_choice - 1) % 3):
        score += your_choice + 1
    else:
        score += your_choice + 1 + 3

print(score)
