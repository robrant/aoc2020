
def process_line(line):
    """ Processes a single line """
    line = line.strip()
    policy,pswd = line.split(':')
    pswd = pswd.strip()
    number_range, pwsd_chr = policy.split(' ')
    chr_pos_1, chr_pos_2 = map(int, number_range.split('-'))

    return pswd, pwsd_chr, chr_pos_1, chr_pos_2

def validate_password(pswd, pwsd_chr, chr_pos_1, chr_pos_2):
    """ Validates the password against policy, not non-zero index """
    valid = False
    if pswd[chr_pos_1-1] == pwsd_chr and pswd[chr_pos_2-1] == pwsd_chr:
        valid = False
    elif pswd[chr_pos_1-1] == pwsd_chr or pswd[chr_pos_2-1] == pwsd_chr:
        valid = True
    return valid

if __name__ == '__main__':

    f = open("day2_input.txt", 'r')
    data = []
    valid_pswds = []
    invalid_pswds = []

    for line in f.readlines():
        pswd, pwsd_chr, chr_pos_1, chr_pos_2 = process_line(line)
        valid = validate_password(pswd, pwsd_chr, chr_pos_1, chr_pos_2)
        if valid == True:
            valid_pswds.append(line)
        else:
            invalid_pswds.append(line)

    print ("Valid: ", len(valid_pswds))
