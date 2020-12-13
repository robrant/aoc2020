

# Read in the whole map into an array

# Loop on the rows (1)
    # Loop on the columns (3)

f = open('./day3_input.txt', 'r')
lines = f.read().split('\n')

# Generate a 2D map, list of lists
tree_map = []
for y in range(len(lines)-1):
    tree_map.append([char for char in lines[y]])

# Setup steppers
x_step = 3
y_step = 1

# Counters
x = 0
y = 0
tree_counter = 0

# Width of tree map
line_length = len(tree_map[0])

# Loop rows
while y < len(tree_map)-1:

    # Get the x index, assumed tree pattern loops right
    x = x % line_length

    print (y, x, tree_map[y][x])
    #tree_map[y][x] = "O" # Mark the route taken
    if tree_map[y][x] == "#":
        tree_counter += 1

    x += x_step
    y += y_step

print (tree_counter)

# Print a pretty version to check the route taken
#for line in tree_map[0:30]:
#     print (''.join(line))