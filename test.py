#class maxGoat():
 #   def __len__(self):
  #      return 4
    
#myGoat = maxGoat
# print(bool(maxGoat))

#final lap, kalo max menang wdc, kalo lewis menang wdc

p1Wdc = 299
p2Wdc = 298
win = 25
runnerUp = 18
p1 = 'lewis'
p2 = 'max'
lap = 56

def addLap():
    global lap
    lap += 1
    
addLap()

crofty = f'now we are entering final lap {lap}'

class wdc():
    def finalLap():
        return True
    
if wdc.finalLap():
    p1 = 'max'
    p2 = 'lewis'
    def winner(w, p):
        return f"{p} wins with {w} point"
    print(winner(win + p2Wdc, p1))
else: 
    def winner(w, p):
        return f"{p} wins with {w} point"
    print(winner(win + p1Wdc, p1))