import os
import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def validate_year(year, min, max):
    valid = False
    year = int(year)
    if len(str(year)) == 4 and year >= int(min) and year <= int(max):
        valid = True
    return valid

def validate_height(height):
    valid = False
    unit = height[-2:]
    hgt = int(height[:-2])

    if unit == 'cm' and hgt >= 150 and hgt <= 193:
        valid = True
    elif unit == 'in' and hgt >= 59 and hgt <= 76:
        valid = True
    return valid

def validate_colour(hcl):
    valid = False
    regexp = "^#([A-Fa-f0-9]{6})$"
    if re.search(regexp, hcl):
        valid = True
    return valid

def validate_eye_colour(ecl):
    valid = False
    ecl = ecl.strip().lower()
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid = True
    return valid

def validate_pid(pid):
    valid = False
    try:
        int(pid)
        if len(pid.strip()) == 9:
            valid = True
    except ValueError:
        valid = False

    return valid

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
    fields_present = []
    fields_not_present = []

    for record in records:
        valid_record = validate_record(record)
        if valid_record:
            valid_counter += 1
            fields_present.append(record)
        else:
            invalid_counter += 1
            fields_not_present.append(record)
    
    # Just work with the records with all fields present
    valid_records = []
    invalid_records = []
    for record in fields_present:
        
        # Validate birth year
        if not validate_year(record['byr'], 1920, 2002):
            invalid_records.append(record)
            continue
        # Validate issue year
        if not validate_year(record['iyr'], 2010, 2020):
            invalid_records.append(record)
            continue
        # Validate expiry year
        if not validate_year(record['eyr'], 2020, 2030):
            invalid_records.append(record)
            continue
        