import time as t        #Импорт библиотек
import os                  # до этого момента
cls = lambda: os.system('cls') #Создание функции для очистки консоли
t.sleep(0.15) #Логотип
print("W E L C O M E");
t.sleep(0.15)
print("Array Sorter on Python 3.0+")
print("Version: 3.5");
t.sleep(0.15)
print("Author: Vitaz145");
t.sleep(0.15)
print("URL: https://vk.com/vitaz145");
t.sleep(3) #Конец логотипа
cls()
try:
    text_file = open("numbers.txt")
except IOError:
    print("!!! Файл массива не найден, создайте файл numbers.txt и заполните его !!!")
    t.sleep(5)
    exit()
text_file = open("numbers.txt", "r") #Открытие файла
Arr1 = text_file.read() #Считывание данных из файла
Arr2 = Arr1.split(",") #Создание нового массива и разделение чисел через запятую(до этого массив был цельный)
NX = len(Arr2) #Нахождение количества чисел в массиве\текстовом файле
cls() #Очистка консоли
print("Массив, который будет сортироваться: ")
if 10 > NX:
    print(Arr2)
else:
    print("(Слишком большой для вывода)")
print("Кол-во чисел: ", NX)
t.sleep(4)
cls() #Очистка консоли
print("От меньшего к большему. (1 / 2)") #Начало сортировки
Arr2.sort(key = int) #Сортировка массива
for x in Arr2:  #Вывод массива
    print(x)
t.sleep(1)
print()
print("От большего к меньшему. (2 / 2)")
Arr2.sort(reverse = True, key = int) #Зеркалирование массива
for x in Arr2:  #Вывод массива
    print(x)
print()
t.sleep(2)
print("Нажмите Enter для выхода.") #Конец сортировки
ext = input() #Запрос ввода (ожидание нажатия Enter)
exit() #Выход

