x=0
p = input("болит у тебя голов? ")
z = input("заложен у тебя нос? ")
y = input("если у тебя температура? ")
n = input("слезяца у тебя глаза? ")
#print (p, z, y, n)
#p='да'
if (p == 'да'):
    x=x+1
    #print(x)
if (z == "да"):
    x=x+1
    #print(x)
if (y == "да"):
    x=x+1
    #print(x)
if (n == "да"):
    x=x+1
    #print(x)
    
if (x == 4):
    print("Раз вас болит голова и заложен нос и есть температура и слезится глаза то нужно обратится к доктору ")

if ( x == 3):
    print("нужно спросить у мамы")

if (x == 0):
    print("если нет симтомов болезни то тогда нужно вывести: по анкетным данным которые вы вводили голова у вас не болит температуры нет глаза не слизятся то тогда можно идти гулять")