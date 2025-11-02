#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
z=1
q=2
cymma=2
spisok =[q]
for x in range (0,50):
    
    w=z+q
    print(w,z,q,0000)
    
    #w=(spisok[z])
    #if z=q+w:
    if w%2==0:  
        spisok.append(w)
        if cymma<1100000:
            cymma=cymma+w
    print (w,z,q)
    q=w
    z=w-z
    print(w,z,q) 
        #x=spisok[z-1]+ spisok[z]
        
print(spisok)
print(cymma)
