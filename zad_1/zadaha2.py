#Даны списки: 
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# https://dev-gang.ru/article/lambda-map-i-filter-v-python/
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#Нужно вернуть список, который состоит из элементов, 
#общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(filter(lambda elem: elem in b, a))
print(result)


for x in a:
    if x < 5:
        print(x)