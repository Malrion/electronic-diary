# Electronic diary (In Python) v2.0
# Powered by Marat Remushev

Mon = ['Monday -']
Tue = ['Tuesday -']
Wed = ['Wednesday -']
Th = ['Thursday -']
Fr = ['Friday -']
Sat = ['Saturday -']
Sun = ['Sunday -']
journal = [Mon, Tue, Wed, Th, Fr, Sat, Sun]

# 1 task
a = 0
print('=' * 100)
for i in range(7):
    a += 1
    journal[-1 + a] .append('No cases')

print(journal)
print('=' * 100)

while True:
    line = input('Enter the command:')

    # Print command
    if (line == 'print'):
        print('Weekly calendar:' + str(journal))

    # Check command
    if (line == 'check'):
        print('1 - Monday')
        print('2 - Tuesday')
        print('3 - Wednesday')
        print('4 - Thursday')
        print('5 - Friday')
        print('6 - Saturday')
        print('7 - Sunday')
        choice = input('What day of the week do you want to watch?')
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

    # Edit command
    def edit(day):
        del day[1]
        day.append(ed)
        print('Case changed!')
        print()

    if (line == 'edit'):
        print('1 - Monday')
        print('2 - Tuesday')
        print('3 - Wednesday')
        print('4 - Thursday')
        print('5 - Friday')
        print('6 - Saturday')
        print('7 - Sunday')
        choice = input('Which day of the week do you want to choose?')
        ed = input('Enter the purpose of the case:')
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
        print('Case changed!')
        print()

    # Delete command
    def delete(day):
        del day[1]
        day.append('No to do')
        print('Case deleted!')
        print()

    if (line == 'delete'):
        print('1 - Clear case')
        print('2 - Reset to-do list')
        choice = input('Choose an option:')
        if choice == '1':
            print('1 - Monday')
            print('2 - Tuesday')
            print('3 - Wednesday')
            print('4 - Thursday')
            print('5 - Friday')
            print('6 - Saturday')
            print('7 - Sunday')
            choice = input('What case do you want to clear?')
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
            print('1 - Yes')
            print('2 - No')
            choice = input('Are you sure you want to nullify the list?')
            if choice == '1':
                del Mon[1]
                Mon.append('No cases')
                del Tue[1]
                Tue.append('No to do')
                del Wed[1]
                Wed.append('No cases')
                del Th[1]
                Th.append('No cases')
                del Fr[1]
                Fr.append('No cases')
                del Sat[1]
                Sat.append('No cases')
                del Sun[1]
                Sun.append('No cases')
                print('To-do list has been cleared!')
                print()

            if choice == '2':
                continue

    # Help command
    if (line == 'help'):
        print(''' 1) "print" - Display the calendar for the week
2) "check" - View the case
3) "edit" - Change the case
4) "delete" - Zero or clear the case
5) "help" - View the list of commands
''')
