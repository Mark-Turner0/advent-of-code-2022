def main():
    f = open("input", 'r')
    grid = f.read().split()
    f.close()

    visible = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if is_visible(grid[row][column], grid[row][:column]):
                visible += 1
            elif is_visible(grid[row][column], grid[row][column + 1:]):
                visible += 1
            else:
                trees_for_row = ""
                for each_row in grid[:row]:
                    trees_for_row += each_row[column]
                if is_visible(grid[row][column], trees_for_row):
                    visible += 1
                else:
                    trees_for_row = ""
                    for each_row in grid[row + 1:]:
                        trees_for_row += each_row[column]
                    if is_visible(grid[row][column], trees_for_row):
                        visible += 1

    print(visible)


def is_visible(tree, other_trees):
    if True in map(lambda x: int(x) >= int(tree), other_trees):
        return False
    return True


if __name__ == "__main__":
    main()
