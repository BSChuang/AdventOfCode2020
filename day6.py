file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n\n')
def partOne(inp):
    inp = [x.replace('\n', '') for x in inp]
    
    count = 0
    for str in inp:
        count += len(set([char for char in str]))

    return count

def partTwo(inp):
    count = 0
    for str in inp:
        groupList = str.split('\n')
        groupList = [set([char for char in group]) for group in groupList]

        intersect = groupList[0].intersection(*groupList)
        
        count += len(intersect)
    
    return count

print(partTwo(inp))