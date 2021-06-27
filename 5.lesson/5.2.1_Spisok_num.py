#Задача отсортировать список

numbers = [4,3,65,83,45,76,34,11,35,84,23,315]

# По возврастанию

numbers.sort()
print(numbers)

# По убыванию
numbers.sort(reverse=True)
print(numbers)

# Заменить Элемени в списке
numbers[1] = "B"
print(numbers)
