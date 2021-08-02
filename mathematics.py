# математика для самых маленьких

a = 5
b = 6

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a ** b)

try:
    a = int(input('Первое число:'))
    b = int(input('Второе число:'))
    znak = input('Что с ними сделать?')
    res = "Ваш ответ: "
except ValueError:
    print("Ошибка: введите число")
else:
    if znak == "":
        print('Ошибка: введите действие, которое хотите совершить. На выбор:"+", "-", "*" и "/"')
    try:
        if znak == "+":
            print(res, a + b)
        elif znak == "-":
            print(res, a - b)
        elif znak == "*":
            print(res, a * b)
        elif znak == "/":
            print(res, a / b)
    except ZeroDivisionError:
        print("Ошибка: нельзя делить на ноль.")
