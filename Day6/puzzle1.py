f = open("input", 'r')
input_str = f.read()
f.close()

for character in range(len(input_str) - 4):
    if len(set(input_str[character:character + 4])) == len(input_str[character:character + 4]):
        print("Marker found at", character + 4)
        break
