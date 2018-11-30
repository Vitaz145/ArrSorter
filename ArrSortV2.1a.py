import os
cls = lambda: os.system('cls')
import time as t
print("Напишите кол-во чисел в массиве: ")
NX = int(input())
Arr1 = [0]
cls()
for i in range(1, NX + 1):
    print("Введите ", i, " число массива.", "(", i, "/", NX, ")")
    cache = int(input("Ввод: "))
    Arr1.append(cache)
    cls()
Choose = input("Bubble sort? n = нет ")
cls()
if Choose.upper() == 'N':
    print("От меньшего к большему. (1 / 2)")
    Arr1.sort()
    for x in Arr1:
        print(x)
    t.sleep(1)
    print()
    print("От большего к меньшему. (2 / 2)")
    Arr1.sort(reverse = True)
    for x in Arr1:
        print(x)
    print()
    t.sleep(2)
    print("Нажмите Enter для выхода.")
else:
    print("Bubble Sort. (1 / 2)")
    n = 1
    while n < len(Arr1):
        for i in range(len(Arr1)-n):
            if Arr1[i] > Arr1[i+1]:
                Arr1[i], Arr1[i+1] = Arr1[i+1], Arr1[i]
        n += 1
    for x in Arr1:
      print(x)
    print()
    print()
    t.sleep(1)
    print("Bubble Sort reverse. (2 / 2)")
    Arr1.sort(reverse = True)
    for x in Arr1:
      print(x)
    print()
    t.sleep(2)
    print("Нажмите Enter для выхода.")
ext = input()
exit()
