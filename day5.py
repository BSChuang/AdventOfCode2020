import math

file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

def partOne(inp):
    maxSeat = 0
    for seat in inp:
        idBot = 0
        idTop = 127
        for char in seat[:7]:
            diff = (idTop - idBot) / 2
            if char == 'F':
                idTop -= math.ceil(diff)
            else:
                idBot += math.ceil(diff)
        
        idLeft = 0
        idRight = 7
        for char in seat[7:]:
            diff = (idRight - idLeft) / 2
            if char == 'L':
                idRight -= math.ceil(diff)
            else:
                idLeft += math.ceil(diff)

        maxSeat = max(maxSeat, idBot * 8 + idLeft)
    return maxSeat

def partTwo(inp):
    seatList = []
    for seat in inp:
        idBot = 0
        idTop = 127
        for char in seat[:7]:
            diff = (idTop - idBot) / 2
            if char == 'F':
                idTop -= math.ceil(diff)
            else:
                idBot += math.ceil(diff)
        
        idLeft = 0
        idRight = 7
        for char in seat[7:]:
            diff = (idRight - idLeft) / 2
            if char == 'L':
                idRight -= math.ceil(diff)
            else:
                idLeft += math.ceil(diff)

        seatList.append(idBot * 8 + idLeft)
    
    print(sorted(seatList))
    minSeat = min(seatList)
    for i, seatId in enumerate(sorted(seatList)):
        if seatId != i + minSeat:
            return seatId

print(partTwo(inp))