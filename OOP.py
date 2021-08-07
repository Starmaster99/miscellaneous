# ООП для самых маленьких


print("Мы - объектно-ориентированная компания по сбору ПК! Прежде всего мы ориентируемся на параметры компонентов, "
      "а уже потом на цену. Перечислите нужные Вам параметры и мы соберём ПК идеально подходящий для Вас!")
cores = input("Сколько ядер будет у процессора? ").strip()
vmemory = input("Сколько видеопамяти будет у Вашей видеокарты? ").strip()
ram = input("Сколько оперативной памяти будет у компьютера? ").strip()
hmemory = input("Сколько всего будет памяти у ПК? В гигабайтах. ").strip()


# немного терминологии

class Computer:                                        # это - класс
    def __init__(self, cores, vmemory, ram, hmemory):  # инициализируем класс
        self.cores = cores                             # это - атрибут класса
        self.vmemory = vmemory
        self.ram = ram
        self.hmemory = hmemory

    def __str__(self):  # это то, как себя будет вести класс в print()
        return "Итого: \n%s ядер, %s видеопамяти, %s ОЗУ, %s места на жёстких дистах." \
               "\nВсе правильно?" % (cores, vmemory, ram, hmemory)


c = Computer(cores, vmemory, ram, hmemory)
print(c)
