# ООП для самых маленьких
# TODO: в конце концов понять как работают классы и сделать что-нибудь ещё


print("Мы - объектно-ориентированная компания по сбору ПК! Прежде всего мы ориентируемся на параметры компонентов, "
      "а уже потом на цену. Перечислите нужные Вам параметры и мы соберём ПК идеально подходящий для Вас!")
cores = input("Сколько ядер будет у процессора? ").strip()
vmemory = input("Сколько видеопамяти будет у Вашей видеокарты? ").strip()
ram = input("Сколько оперативной памяти будет у компьютера? ").strip()
hmemory = input("Сколько всего будет памяти у ПК? В гигабайтах. ").strip()


class Computer:
    # computers = 0
    def __init__(self, cores, vmemory, ram, hmemory):  # инициализируем класс
        self.cores = cores
        self.vmemory = vmemory
        self.ram = ram
        self.hmemory = hmemory
        # Computer.computers += 1

    def __str__(self):
        return "Итого: \n%s ядер, %s видеопамяти, %s ОЗУ, %s места на жёстких дистах.\nВсе правильно?" % (cores, vmemory, ram, hmemory)


c = Computer(cores, vmemory, ram, hmemory)
print(c)
