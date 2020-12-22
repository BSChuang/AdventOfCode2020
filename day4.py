file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n\n')
inp = [x.replace('\n', ' ') for x in inp]

def partOne(inp):
    valid = 0
    for passport in inp:
        isValid = True
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if field not in passport:
                isValid = False
                break
        valid += 1 if isValid else 0

    return valid

def partTwo(inp):
    valid = 0
    for passport in inp:
        passport = parsePassport(passport)
        valid += 1 if validate(passport) else 0
    return valid
        
def validate(passport): # passport must be parsed
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in passport:
            return False
    if not validateYear(passport['byr'], 4, 1920, 2002):
        #print(passport['byr'], validateYear(passport['byr'], 4, 1920, 2002))
        return False
    if not validateYear(passport['iyr'], 4, 2010, 2020):
        #print(passport['iyr'], validateYear(passport['iyr'], 4, 2010, 2020))
        return False
    if not validateYear(passport['eyr'], 4, 2020, 2030):
        #print(passport['eyr'], validateYear(passport['eyr'], 4, 2020, 2030))
        return False
    if not validateHgt(passport['hgt']):
        #print(passport['hgt'], validateHgt(passport['hgt']))
        return False
    if not validateHcl(passport['hcl']):
        #print(passport['hcl'], validateHcl(passport['hcl']))
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(passport['ecl'], passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        return False
    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        return False
    return True
    

def validateYear(year, length, minimum, maximum):
    return len(year) == length and year.isdigit() and minimum <= int(year) <= maximum

def validateHgt(hgt):
    if 'cm' in hgt:
        hgt = hgt.replace('cm', '')
        return hgt.isdigit() and 150 <= int(hgt) <= 193
    elif 'in' in hgt:
        hgt = hgt.replace('in', '')
        return hgt.isdigit() and 59 <= int(hgt) <= 76
    else:
        return False

def validateHcl(hcl):
    if hcl[0] != '#' or len(hcl[1:]) != 6:
        return False
    try:
        int(hcl[1:], 16)
        return True
    except ValueError:
        return False

def parsePassport(passport):
    passList = passport.split()
    passList = [x.split(':') for x in passList]
    passDict = {x[0] : x[1] for x in passList}

    return passDict

print(partTwo(inp))