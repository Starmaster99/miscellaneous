# функции для самых маленьких

user_list = []

try:
    print("Назови мне список чисел, и я посчитаю их сумму!")
    n = input("Сколько их будет всего? ").strip()
    n = int(n)
    print("А теперь назови их самих")
    for n in range(0, n):
        user_var = int(input())
        user_list.append(user_var)

except ValueError:
    print("Писать можно только цифры!")


def main(user_list):
    return sum(user_list)


a = main(user_list)
print(f"Сумма ваших чисел составляет {a}!")


def hello():
    name = input("Как мне тебя называть? ").capitalize()
    return name

def hi(name):
    print(f"Приветствую, {name}!")

hi(hello())
