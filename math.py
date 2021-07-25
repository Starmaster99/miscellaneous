# математика для самых маленьких

# a = 5
# b = 6

# plus = a+b
# print(plus)

# minus = a-b
# print(minus)

# mult = a*b
# print(mult)

# div = a/b
# print(div)

# power = a**b
# print(power)

# TODO: калькулятор

a=int(input('Первое число: '))
b=int(input('Второе число: '))
znak=input('Что с ними сделать? ')
res="Ваш ответ: "

if znak == "+":
    print(res, a+b)
elif znak == "-":
    print(res, a-b)
elif znak == "*":
    print(res, a*b)
elif znak == "/":
    print(res, a/b)
else:
    print('Введите нужное действие')








