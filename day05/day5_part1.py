
# Function:
#    input: character, min, max,
#    output: min, max

def get_new_range(char, min_in=0, max_in=127):
    """ Get a new subset range for rows and columns """

    in_range = int(max_in) - int(min_in)
    mid_point = min_in + int(in_range / 2)

    if char.lower() in ['f', 'l']:
        min_out = min_in
        max_out = mid_point
    elif char.lower() in ['b', 'r']:
        min_out = mid_point + 1
        max_out = max_in

    return [min_out, max_out]

def get_row_id(boarding_pass):

    row_data = boarding_pass[:-3]
    min_in = 0
    max_in = 127
    for char in row_data:
        min_in, max_in = get_new_range(char, min_in, max_in)
        if min_in == max_in:
            return min_in

def get_col_id(boarding_pass):

    col_data = boarding_pass[-3:]
    min_in = 0
    max_in = 7
    for char in col_data:
        min_in, max_in = get_new_range(char, min_in, max_in)
        if min_in == max_in:
            return min_in

def get_seat_id(row_id, col_id):
    return int(row_id) * 8 + col_id

if __name__ == '__main__':
    
    f = open('./day5_input.txt', 'r')
    
    seat_ids = []

    for line in f.readlines():

        boarding_pass = line.strip()
        row_id = get_row_id(boarding_pass)
        col_id = get_col_id(boarding_pass)
        seat_id = get_seat_id(row_id, col_id)
        seat_ids.append(seat_id)
    
    print (max(seat_ids))