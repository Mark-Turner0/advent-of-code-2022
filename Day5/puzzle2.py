import re

f = open("input", 'r')
input_str = f.read()
f.close()
box_section, instruction_section = input_str.split("\n\n")

instructions = instruction_section.splitlines()

box_rows = box_section.splitlines()
num_columns = len(box_rows.pop().split())

parsed_rows = []

for row in box_rows:
    filtered_row = re.findall(r"( |\[)( |\w)(  |\])", row)
    boxes = [i[1] for i in filtered_row]
    parsed_rows.append(boxes)

parsed_rows.reverse()
stacks = [[]]

for column in range(num_columns):
    new_column = []
    for row in range(len(parsed_rows)):
        box = parsed_rows[row][column]
        if box == " ":
            continue
        new_column.append(parsed_rows[row][column])
    stacks.append(new_column)

for line in instructions:
    _, num_boxes, _, from_pile, _, to_pile = line.split()
    grabbed = [stacks[int(from_pile)].pop(-1) for _ in range(int(num_boxes))]
    grabbed.reverse()
    stacks[int(to_pile)].extend(grabbed)

answer = []

for pile in stacks:
    if len(pile) > 0:
        answer.append(pile[-1])

print(''.join(answer))
