# числа Фибоначчи для самых маленьких

a = 0       # первое число последовательности
b = 1       # второе число
c = 0       # буфер
count = 0   # счётчик

print("Числа Фибоначчи - это элементы числовой последовательности, в которой первые два числа равны 0 и 1, "
      "а последующие равны сумме двух предыдущих.\nНа экран будет выведено 25 чисел.")

print(a)

for count in range(12):
    b = c + b
    print(b)
    c = b + c
    print(c)
