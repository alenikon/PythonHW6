# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

NumberS = int(input("Введите шестизначный номер билета:"))

First = int(NumberS /100000) %10
Second = int(NumberS /10000) %10
Third = int(NumberS /1000) %10
Fourth = int(NumberS /100) %10
Fifth = int(NumberS /10) %10
Sixth = int(NumberS) %10

print(First, Second, Third, Fourth, Fifth, Sixth)

if First+Second+Third == Fourth+Fifth+Sixth:
    print(NumberS, "-> yes")
else: print(NumberS, "-> no")