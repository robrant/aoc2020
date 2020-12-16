import os

def validate_record(record):
    """ Check whether fields are present """
    
    valid = False

    # The fields to check
    flds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    diff = set(record.keys()) ^ set(flds)
    
    # Ignore the optional field, cid
    diff.discard('cid')

    if len(diff) == 0:
        valid = True

    return valid

def process_record(raw_record):
    """ Process a possible passport record into a dict """

    record = {}
    
    raw_record = raw_record.replace(os.linesep, ' ')
    field_record = raw_record.split(' ')
    print (field_record)
    for fld in field_record:
        fld = fld.split(':')
        try:
            record[fld[0]] = fld[1]
        except IndexError:
            continue
    return record

if __name__ == '__main__':
    
    # Read file contents and split based on blank line (\n\n)
    f = open('./day4_input.txt', 'r')
    raw_records = f.read().split(os.linesep + os.linesep)
    
    # Process all records into a list of dicts
    records = [process_record(r) for r in raw_records] 
    
    # Check for difference and count
    valid_counter = 0
    invalid_counter = 0
    for record in records:
        valid_record = validate_record(record)
        if valid_record:
            valid_counter += 1
        else:
            invalid_counter += 1
    
    print (valid_counter, invalid_counter)