import math

def count_trees(tree_map, y_step, x_step):
    """ Count the trees hit on a slope, defined by the step args """

    # Counters
    x = 0
    y = 0
    tree_counter = 0

    # Width of tree pattern
    line_length = len(tree_map[0])

    # Loop rows
    while y < len(tree_map)-1:

        # Get the x index, assumed tree pattern loops right
        x = x % line_length

        #tree_map[y][x] = "O" # Mark the route taken
        if tree_map[y][x] == "#":
            tree_counter += 1

        x += x_step
        y += y_step

    return tree_counter


if __name__ == '__main__':

    f = open('./day3_input.txt', 'r')
    lines = f.read().split('\n')

    # Generate a 2D map, list of lists
    tree_map = []
    for y in range(len(lines)-1):
        tree_map.append([char for char in lines[y]])

    # Slope definitions 
    slopes = [[1,1],
              [1,3],
              [1,5],
              [1,7],
              [2,1]]

    trees_encountered = []
    for slope in slopes:
        trees = count_trees(tree_map, slope[0], slope[1])
        trees_encountered.append(trees)

print (trees_encountered)
product = 1
for x in trees_encountered:
    product *= x
print (product)


# Print a pretty version to check the route taken
#for line in tree_map[0:30]:
#     print (''.join(line))