import random
p=n=0
for i in range(1,11):
    b=random.randint(1,10)
    a=random.randint(1,10)
    v=a*b
    print (a,"X",b)
    s=int(input("назави умножение: "))
    print (s)
    print (v)
    if s==v:
        print("Правильно")
        
        p=p+1 
        print (p)
    else:
        print("Не верно")
        
        n=n+1
        print(n)
print ("правильных ответов", p)
print ("не правильных ответов", n)
print(i)