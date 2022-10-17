# "karakteres" - string (karakterlánc)
a:str = 'valami'
b:str = "valami"

print("Don't give up!")
print('"Sárga füvek a homkon"')

# konkatenáció (összefűzés)
print('kutya' + 'ház') # -> 'kutyaház'
print(3 * 'cica ') # -> 'cica cica cica '

# numerikus típusok:
# - integer (egész szám)
c:int = 10
# - floating point number ("valós" szám)
d:float = 3.14
print(10 + 3) # -> 13
print(10 - 3) # ->  7
print(10 * 3) # -> 30

print(10 /  3) # -> 3.3333... 'sima' osztás
print(10 // 3) # -> 3          egész osztás     [div]
print(10 %  3) # -> 1          maradékszámítás  [mod]

print(2 ** 10)  # -> 1024      hatványozás
print(16 ** .5) # -> 4.0       "gyökvonás" (az azonosság miatt)

# int és float ún. "típuskompatibilis" az operátorok tekintetében
print(10 / 1.5)


# logikai - Boolean
e:bool = True
f:bool = False

print(True and False) # -> F
print(True  or False) # -> T
print(     not  True) # -> F

# compare aka. "összehasonlító" operátorok
# numerikus alkalmazás:
print(10 <  3)         # -> F
print(10 <= 3)         # -> F
print(10 >  3)         # -> T
print(10 >= 3)         # -> T

# általános alkalmazás:
print('cica' == 'kutya')  # -> F
print(10 == 3)            # -> F
print(False == False)     # -> T

print('cica' != 'kutya')  # -> T
print(10 != 3)            # -> T
print(False != False)     # -> F

print('kecske' != 'káposzta' or 20 <= 12)  # -> T

# "tartalmazza", "eleme", "benne van"...
# <érték> in <kollekció> -> logikai

print(3 in [11, 42, 61, 4, 2, 3, 33, 10])  # -> T
print('a' not in {'e', 'f', 'D', 'G'})     # -> T