file = open('input.txt', 'r')
inp = file.read()
file.close()

# Cleaning input list
inp = inp.split()
inp = [int(x) for x in inp] # List of string --> list of int

def partOne(inp, mySum):
    looked = []
    for num in inp:
        if mySum - num in looked: # We want A + B = 2020. Therefore we can see if 2020 - A to get B, and see if B is in the list
            return num * (mySum - num)
        looked.append(num)
    return None

def partTwo(inp, mySum):
    looked = []
    for num in inp:
        # We want A + B + C = 2020. We can pass 2020 - A which is equal to B + C into the function from partOne. partOne will return 
        # a number if two numbers in the analyzed list sum to B + C. 
        twoSum = partOne(looked, mySum - num)
        if twoSum != None:
            return num * twoSum
        looked.append(num)
    
print(partOne(inp, 2020))
print(partTwo(inp, 2020))