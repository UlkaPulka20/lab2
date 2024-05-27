import random

#1
password = input("Введите пароль: ")
password_harder = input("Повторите пароль: ")

if password == password_harder:
        print("Пароль принят")
else:
        print("Пароль не принят. Попробуйте еще раз.")

#2
place_number = None

while not place_number:
        place_number = input("Место: ")

if int(place_number) in range(37, 55):
        print("Место боковое")

if int(place_number) % 2 == 0:
        print("Место верхнее")

else:
        print("Место нижнее")

#3
def lab2():
    month = None

    try:
        while not month:
            month = input("Введите год: ")

        if (int(month) % 4 == 0 and int(month) % 100 != 0) or int(month) % 400 == 0:
            print("Год {month} високосный.")
            print("Год {month} високосный.")
        else:
            print("Год {month} не високосный.")
    except ValueError:
        print("Введите  только число")

#4
COLORS = ("красный", "синий", "желтый")


color1 = random.randrange(0, 3)
color2 = random.randrange(0, 3)

if color1 == color2:
        print(COLORS[color1])


if (color1 == 0 or color2 == 0) and (color1 == 1 or color2 == 1):
        print("Фиолетовый")
elif (color1 == 0 or color2 == 0) and (color1 == 2 or color2 == 2):
        print("Оранжевый")
elif (color1 == 1 or color2 == 1) and (color1 == 2 or color2 == 2):
        print("Зеленый")
else:
        print("ошибка!")
