f = open("input", 'r')
all_lines = f.readlines()
f.close()

pwd = []
dir_size = {}

for line in all_lines:
    if line.startswith("$ cd"):
        parsed_dir = line.strip()[5:]
        if parsed_dir == "..":
            pwd.pop()
        else:
            pwd.append(parsed_dir)
    elif line.startswith('$') or line.startswith("dir"):
        continue
    else:
        for directory in range(len(pwd)):
            path = '/'.join(pwd[:directory + 1])
            try:
                dir_size[path] += int(line.split()[0])
            except KeyError:
                dir_size[path] = int(line.split()[0])

filtered_dirs = filter(lambda x: x <= 100_000, dir_size.values())
print(sum(filtered_dirs))
