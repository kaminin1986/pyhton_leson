#Дано пятизначное число. Цифры на четных позициях занулить. Например, из 12345 получается число 10305.
x = int(12345)
print(x-x//1000%10*1000-x//10%10*10)