from collections import Counter

f = open("day2_input.txt", 'r')
data = []
valid_pswds = []
invalid_pswds = []

for line in f.readlines():
    line = line.strip()
    
    policy,pswd = line.split(':')
    pswd = pswd.strip()
    
    number_range, pwsd_chr = policy.split(' ')
    min_chr, max_chr = map(int, number_range.split('-'))

    chr_count = Counter(pswd)
    
    if chr_count[pwsd_chr] >= min_chr and chr_count[pwsd_chr] <= max_chr:
        valid_pswds.append(line)
    else:
        invalid_pswds.append(line)

print (len(valid_pswds), len(invalid_pswds))

# for vpwd in valid_pswds:
#     print (vpwd)

# count the number of instances of a character
# evaluate between 2 numbers

