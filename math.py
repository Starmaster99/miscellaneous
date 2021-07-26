# математика для самых маленьких

a = 5
b = 6

print(a+b)

print(a-b)

print(a*b)

print(a/b)

print(a**b)

# TODO: калькулятор

a=int(input('Первое число: '))
b=int(input('Второе число: '))
znak=input('Что с ними сделать? ')
res="Ваш ответ: "

try:
    if znak == "+":
        print(res, a+b)
    elif znak == "-":
        print(res, a-b)
    elif znak == "*":
        print(res, a*b)
    elif znak == "/":
        print(res, a/b)
except(ZeroDivisionError):
    print("Ошибка: нельзя делить на ноль.")


