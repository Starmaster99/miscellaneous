# гороскоп для самых маленьких

mon = input("Введите число месяца вашего рождения: ")

if mon == "":
    print("Ошибка: заполните это поле.")
else:
    try:
        mon = int(mon)
    except(ValueError):
        print("Ошибка: вводите числа.")
    if mon == 0:
        print("Ошибка: введите числа.")
    else:
        if mon == 4:
            print('Вы - Овен.\nВам соответствует стихия Огня.\nВаша планета - Марс.\nДрагоценный камень, подходящий вам больше всего - это Опал.')
        elif mon == 5:
            print('Вы - Телец.\nВам соответствует стихия Земли.\nВаша планета - Венера.\nДрагоценный камеь, подходящий вам больше всего - это Сапфир.')
        elif mon == 6:
            print('Вы - Близнецы.\nВам соответствует стихия Воздуха.\nВаша планета - Меркурий.\nДрагоценный камень, подходящий вам больше всего - это Агат.')
        elif mon == 7:
            print('Вы - Рак.\nВам соответствует стихия Воды.\nВаша планета - Луна.\nДрагоценный камень, подходящий вам больше всего - это Изумруд.')
        elif mon == 8:
            print('Вы - Лев.\nВам соответствует стихия Огня.\nВаша планета - Солнце.\nДрагоценный камень, подходящий вам больше всего - это Оникс.')
        elif mon == 9:
            print('Вы - Дева.\nВам соответствует стихия Земли.\nВаша планета - Меркурий.\nДрагоценный камень, подходящий вам больше всего - это Карнеол.')
        elif mon == 10:
            print('Вы - Весы.\nВам соответствует стихия Воздуха.\nВаша планета - Венера.\nДрагоценный камень, подходящий вам больше всего - это Хризолит.')
        elif mon == 11:
            print('Вы - Скорпион.\nВам соответствует стихия Воды.\nВаша планета - Плутон.\nДрагоценный камень, подходящий вам больше всего - это Берилл.')
        elif mon == 12:
            print('Вы - Стрелец.\nВам соответствует стихия Огня.\nВаша планета - Юпитер.\nДрагоценный камень, подходящий вам больше всего - это Алмаз.')
        elif mon == 1:
            print('Вы - Козерог.\nВам соответствует стихия Земли.\nВаша планета - Сатурн.\nДрагоценный камень, подходящий вам больше всего - это Рубин.')
        elif mon == 2:
            print('Вы - Водолей.\nВам соответствует стихия Воздуха.\nВаша планета - Уран.\nДрагоценный камень, подходящий вам больше всего - это Гранат.')
        elif mon == 3:
            print('Вы - Рыбы.\nВам соответствует стихия Воды.\nВаша планета - Нептун.\nДрагоценный камень, подходящий вам больше всего - это Аметист.')

