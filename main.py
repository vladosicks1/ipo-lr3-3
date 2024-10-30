day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

if month == 4 or month == 6 or month == 9 or month == 11:
    if day > 30:
        print("Дата введена неверно.")
        exit(0)

if day > 31 or day < 1 or month > 12 or month < 1:
    print("Дата введена неверно.")

elif month == 2 and day > 28:
    print("Дата введена неверно.")

elif 1 <= month <= 2 or month == 12:
    print("Зима")

elif 3 <= month <= 5:
    print("Весна")

elif 6 <= month <= 8:
    print("Лето")
    
else:
    print("Осень")