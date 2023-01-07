TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000

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

used_space = dir_size['/']
smallest = TOTAL_SPACE

for iter_dir_size in dir_size.values():
    if used_space - iter_dir_size + REQUIRED_SPACE <= TOTAL_SPACE:
        if smallest > iter_dir_size:
            smallest = iter_dir_size

print(smallest)
