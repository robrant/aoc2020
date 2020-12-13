

import requests

# day_1_url = "https://adventofcode.com/2020/day/1/input"
# # Retrieve the data
# r = requests.get(day_1_url)
# print (r.text)

# Also itertools.combinations

f = open("day1_input.txt", 'r')
data = []
for line in f.readlines():
    data.append(int(line.strip()))

sum_to = 2020
for x in data:
    for y in data:
        for z in data:
            if x + y + z == sum_to:
                print (x, y, z)
                print ("Answer :", x * y * z)
                break