current_lap = 0

p1 = 'max'
p2 = 'lewis'

def addLap():
    global current_lap #manggil var lap seakrang
    current_lap += 1
    
addLap()
addLap()

crofty = f'we are entering lap {current_lap}'

print(crofty)

addLap()
print(f'{p1} still leading the race')

beforeFight = p1, p2 #make sure variable p1 dan p2 diisi orang yang sama
fight = " and ".join(beforeFight)

addLap()

crofty = f'and now we see {fight}, are now fighting at lap {current_lap}'

class fight():
    def battleWin():
        return 0
    addLap()
    print(f'in lap {current_lap}')
    
if fight.battleWin():
    p1 = 'lewis'
    p2 = 'max'
    print(f'{p1} WIN THE AZERBAIJAN GRAND PRIX')
else:
    print(f'{p1} WIN THE AZERBAIJAN GRAND PRIX')