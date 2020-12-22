file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

def parsePassword(inp):
    """
    inp: policy with password
    returns if password passes
    """
    passRange, passChar, password = inp.split()
    passRange = [int(x) for x in passRange.split('-')] # list where 0 index is min and 1 index is max
    passChar = passChar[0] # Getting rid of following colon
    return passRange, passChar, password

def partOne(inp):
    """
    inp: list of password polcies + password in format: '[min instance]-[max instance] [character]: password'
    returns number of passwords which pass their respective policy
    """

    def testPassword(passPolicy):
        passRange, passChar, password = parsePassword(passPolicy)
        countChar = password.count(passChar) # number of char occurrences
        return passRange[0] <= countChar <= passRange[1] # return True if in range, false otherwise

    return sum([testPassword(x) for x in inp]) # Get list of booleans, sum trues
    
def partTwo(inp):
    def testPassword(passPolicy):
        passRange, passChar, password = parsePassword(passPolicy)
        minMatch = password[passRange[0] - 1] == passChar # One index? What is this, Matlab?
        maxMatch = password[passRange[1] - 1] == passChar
        return (minMatch != maxMatch) # Return true of only one position matches

    return sum([testPassword(x) for x in inp]) # Get list of booleans, sum trues
    
print(partTwo(inp))