def main():
    f = open("input", 'r')
    grid = f.read().split()
    f.close()

    current_max = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            column_before = reversed(grid[row][:column])
            scenic_score = visible_trees(grid[row][column], column_before)
            column_after = grid[row][column + 1:]
            scenic_score *= visible_trees(grid[row][column], column_after)

            trees_for_row = ""
            for each_row in grid[:row]:
                trees_for_row = each_row[column] + trees_for_row
            scenic_score *= visible_trees(grid[row][column], trees_for_row)

            trees_for_row = ""
            for each_row in grid[row + 1:]:
                trees_for_row += each_row[column]
            scenic_score *= visible_trees(grid[row][column], trees_for_row)

            if scenic_score > current_max:
                current_max = scenic_score

    print(current_max)


def visible_trees(tree, other_trees):
    viewing_distance = 0
    other_trees = list(other_trees)
    for single_tree in other_trees:
        viewing_distance += 1
        if int(tree) <= int(single_tree):
            break
    return viewing_distance


if __name__ == "__main__":
    main()
