#Удалени пробелов в начале текста и в конце текста
strok = ('       Привет Мир!!!          ')
print(strok.strip()) #strip удаляет пробелы справа и слева от текста
strok1 = ('       Привет Мир!!!                 ')
print(strok1)
print(strok1.lstrip()) #lstrip удаляет пробелы с лева от текста
strok2 = ('       Привет Мир!!!                                                    ')
print(strok2)
print(strok2.rstrip()) #rstrip удаляет пробелы с право от текста
