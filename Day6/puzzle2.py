f = open("input", 'r')
input_str = f.read()
f.close()

DISTINCT = 14

for character in range(len(input_str) - DISTINCT):
    if len(set(input_str[character:character + DISTINCT])) == len(input_str[character:character + DISTINCT]):
        print("Marker found at", character + DISTINCT)
        break
