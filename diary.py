# Electronic diary (На Python) v2.0
# Powered by Marat Remushev

import time

Mon = ['Понедельник -']
Tue = ['Вторник -']
Wed = ['Среда -']
Th = ['Четверг -']
Fr = ['Пятница -']
Sat = ['Суббота -']
Sun = ['Воскресенье -']
journal = [Mon, Tue, Wed, Th, Fr, Sat, Sun]

# 1 задание
a = 0
print('=' * 100)
for i in range(7):
    a += 1
    journal[-1 + a].append('Нет дел')

print(journal)
print('=' * 100)

while True:
    line = input('Введите команду: ')

    # Команда Print
    if (line == 'print'):
        print('Календарь на неделю: ' + str(journal))

    # Команда Check
    if (line == 'check'):
        print('1 - Понедельник')
        print('2 - Вторник')
        print('3 - Среда')
        print('4 - Четверг')
        print('5 - Пятница')
        print('6 - Суббота')
        print('7 - Воскресенье')
        choice = input('Какой день недели вы хотите посмотреть?')
        if choice == '1':
            print(Mon)
        if choice == '2':
            print(Tue)
        if choice == '3':
            print(Wed)
        if choice == '4':
            print(Th)
        if choice == '5':
            print(Fr)
        if choice == '6':
            print(Sat)
        if choice == '7':
            print(Sun)

    # Команда Edit
    def edit(day):
        del day[1]
        day.append(ed)
        print('Дело изменено!')
        print()

    if (line == 'edit'):
        print('1 - Понедельник')
        print('2 - Вторник')
        print('3 - Среда')
        print('4 - Четверг')
        print('5 - Пятница')
        print('6 - Суббота')
        print('7 - Воскресенье')
        choice = input('Какой день недели вы хотите выбрать?')
        ed = input('Введите цель дела: ')
        if choice == '1':
            edit(Mon)
        if choice == '2':
            edit(Tue)
        if choice == '3':
            edit(Wed)
        if choice == '4':
            edit(Th)
        if choice == '5':
            edit(Fr)
        if choice == '6':
            edit(Sat)
        if choice == '7':
            edit(Sun)

    def delete(day):
        del day[1]
        day.append(ed)
        print('Дело изменено!')
        print()

    # Команда Delete
    def delete(day):
        del day[1]
        day.append('Нет дел')
        print('Дело удалено!')
        print()

    if (line == 'delete'):
        print('1 - Очистить дело')
        print('2 - Обнулить список дел')
        choice = input('Выберете опцию: ')
        if choice == '1':
            print('1 - Понедельник')
            print('2 - Вторник')
            print('3 - Среда')
            print('4 - Четверг')
            print('5 - Пятница')
            print('6 - Суббота')
            print('7 - Воскресенье')
            choice = input('Какое дело вы хотите очистить?')
            if choice == '1':
                delete(Mon)
            if choice == '2':
                delete(Tue)
            if choice == '3':
                delete(Wed)
            if choice == '4':
                delete(Th)
            if choice == '5':
                delete(Fr)
            if choice == '6':
                delete(Sat)
            if choice == '7':
                delete(Sun)

        if choice == '2':
            print('1 - Да')
            print('2 - Нет')
            choice = input('Вы действительно хотите обнулить список?')
            if choice == '1':
                del Mon[1]
                Mon.append('Нет дел')
                del Tue[1]
                Tue.append('Нет дел')
                del Wed[1]
                Wed.append('Нет дел')
                del Th[1]
                Th.append('Нет дел')
                del Fr[1]
                Fr.append('Нет дел')
                del Sat[1]
                Sat.append('Нет дел')
                del Sun[1]
                Sun.append('Нет дел')
                print('Список дел обнулен!')
                print()

            if choice == '2':
                continue

    # Команда Help
    if (line == 'help'):
        print('''1) "print" - Вывести календарь на неделю
2) "check" - Посмотреть дело
3) "edit" - Изменить дело
4) "delete" - Обнулить или очистить дело
5) "help" - Посмотреть список команд
''')
