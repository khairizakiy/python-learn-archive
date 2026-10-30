# x = 'python'
# 
# print(x[2:4])
# 
# rgb = ["red", "green", "blue"]
# 
# a, b = 0, 1
# 
# while a < 10:
#     print(a, end=',')
#     a, b = b, a + b
# 
# print(a)

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# x = [a, b]
# 
# y = list(range(1, 10, 3))
# 
# print(y)

# nama = str(input("Enter your name: "))
# 
# panjangNama = len(nama)
#   
# if len(nama) <= 3:
#     print("Your name is too short")
# elif len(nama) >= 20:
#     print("Your name is too long")
# else:
#   print(f"Hello {nama}, welcome to the program!")
#   
# print(f"Your name has {panjangNama} characters.")
# 

# Looping

# pelerPrabowo = ["peler", "prabowo", "ada", "di pantat buntet"]
    
# for peler in pelerPrabowo:
#   print(peler, len(peler))
    
# race = {'Max': 1, 'Lewis': 2, 'Charles': 3, 'Sergio': 4, 'Lando': 5}
# 
# for driver, position in race.copy().items():
#     if position <= 3:
#         print(f"{driver}, Podium")
#     else:
#         print(f"{driver}, Not Podium")

# for driver, position in race.copy().items():
#     if position >= 4:
#         print(f"{driver}, Not Podium")        


# for driver, position in race.copy().items():
#     if position in ['P1', 'P2', 'P3']:
#         print(f"{driver}, Podium")

# for driver, position in race.copy().items():
#     if position in ['P4', 'P5']:
#         print(f"{driver}, Top 5")

# a = ["max", "leclerc", "lewis,", "lando", "perez", "isack"]
# 
# for i in range(len(a)):
#     if a[i] == 'leclerc':
#         print(f'found {a[i]} at index {i}')

# raceRecap = {'max, lewis, leclerc': 'podium', 'lando, perez': 'top 5', 'isack': 'not podium'}
# 
# for driver, position in raceRecap.items():
#     print(f"{driver}, {position}")

# for n in range(3, 100):
#     for x in range(3, n):
#         if n % x == 0:
#             print(f"{n} is equal to {x} * {n // x}")
#             break
#     else:
#         print(f"{n} is prime")

# i = 0
# 
# while i <= 10 :
#     print("*" * i)
#     i += 1

#match case

# raceStatus = 'penonton masuk ke lintasan'
# 
# match raceStatus:
#     case 'red flag' | 'safety car':
#         print("race berhenti")
#     case 'green flag':
#         print('race dimulai')
#     case _:
#         print('double yellow flag')

# class raceGreen:
#     def __init__(self, track, status):
#         self.track = track
#         self.status = status
#         
# class raceYellow:
#     def __init__(self, track, status, driver):
#         self.track = track
#         self.status = status
#         self.driver = driver
# 
# class raceRed:
#     def __init__(self, track, status, driver):
#         self.track = track
#         self.status = status
#         self.driver = driver
# 
# def raceStatus(race):
#     match race:
#         case raceGreen(track=track , status=status):
#             print(f"race masih berjalan {status} flag dengan kondisi lintasan {track}")
#         case raceYellow(track=track, status=status, driver=driver):
#             print(f"race berhenti sementara karena {driver} mengalami insiden di lintasan, dengan kondisi lintasan {track} dan stetward harus memberikan {status} flag")
#         case raceRed(track=track, status=status, driver=driver):
#             print(f"race berhenti total karena {driver} mengalami insiden di lintasan, dengan kondisi lintasan {track} dan stetward harus memberikan {status} flag")
#             
# lap1 = raceGreen("green", "slick")
# lap2 = raceYellow("checo", "sedikit debries", "yellow")
# lap3 = raceRed("leclerc", "mobil di tengah lintasan", "red")
# 
# raceStatus(lap1)
# raceStatus(lap2)
# raceStatus(lap3)
# print("race selesai")

# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# def process_points(points):
#     match points:
#         case []:
#             print("No points")
#         case [Point(0, 0)]:
#             print("The origin")
#         case Point(x, y):
#             print(f"Single point {x}, {y}")
#         case Point(0, y1), Point(0, y2):
#             print(f"Two on the Y axis at {y1}, {y2}")
#         case Point(x, y) if x == y:
#             print(f"y=x at {x}")
#         
# point1 = Point(0, 0)
# point2 = Point(0, 2)
# point3 = Point(1, 1)
# process_points([point1, point2])
# process_points([point3])

#defining functions

# def lap(l):
#     lap = 0
#     while lap < l:
#         lap += 1
#         print(f"current we're at lap {lap}")
#     print()
#     
# lap(8)

def overtake(reply, tries=1):
    while True:
        response = input(reply) 
        if response in ['yes', 'y']:
            print("overtake successful")
        tries += 1
        if tries >= 2:
            break
        if response in ['no', 'n']:
            print("overtake failed")
        tries -= 1
        if tries < 0:
            raise ValueError('crash happened')

overtake("do you want overtake? ")