import re

file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

def partOne(inp):
    rules = {None: []} # Key (str): our bag, val (list of 2tuple (bag quantity, bag name)): bags that key bag can fit inside (not bags that key bag can hold)
    for ruleStr in inp:
        ruleStr = ruleStr.replace('.', '').replace(' bags', '').replace(' bag', '')
        rule = re.split(' contain |, ', ruleStr)

        bigBag = rule.pop(0)

        if 'no other' in rule:
            rules[None].append((1, bigBag))
            continue

        smallBags = [tuple(bag.split(' ', 1)) for bag in rule]

        for smallBag in smallBags:
            bagCount = smallBag[0]
            bagName = smallBag[1]
            
            if bagName not in rules:
                rules[bagName] = []
            rules[bagName].append((bagCount, bigBag))

    myBag = 'shiny gold'

    count = 0
    possible = rules[myBag]
    checked = []
    while len(possible) > 0:
        bag = possible.pop(0)
        bagName = bag[1]
        print(bag, checked)
        if bagName in checked:
            continue

        count += 1
        checked.append(bagName)
        possible += rules[bagName] if bagName in rules else [] 

    return count

def partTwo(inp):
    rules = {} # Key (str): our bag, val (list of 2tuple (bag quantity, bag name)): bags that key bag CAN HOLD

    for ruleStr in inp:
        ruleStr = ruleStr.replace('.', '').replace(' bags', '').replace(' bag', '')
        rule = re.split(' contain |, ', ruleStr)

        bigBag = rule.pop(0)

        if 'no other' in rule:
            rules[bigBag] = None
            continue

        smallBags = [tuple(bag.split(' ', 1)) for bag in rule]

        rules[bigBag] = smallBags

    myBag = 'shiny gold'
    return bagRecursion(rules, myBag) - 1


def bagRecursion(rules, bagName):
    if rules[bagName] == None:
        return 1
    
    bagList = rules[bagName]
    bagCount = 0
    for bag in bagList:
        bagCount += int(bag[0]) * bagRecursion(rules, bag[1])
    return bagCount + 1


print(partTwo(inp))