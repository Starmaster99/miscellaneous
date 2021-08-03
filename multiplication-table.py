# таблицы умножения для самых маленьких

print("Это - таблица умножения.")

try:
    n = int(input("Сколько столбцов должно быть в таблице? ").strip())
    print("-" * 4*n)
except ValueError:
    print("Ошибка: введите целые числа!")


def mult(n):
    for row in range(1, n+1):
        for col in range(1, n+1):
            print(row*col, end="\t")
        print()
    print("-" * 4*n)

mult(n)