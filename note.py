# Bot for Notes (In Python) v1.2
# Powered by Marat Remushev

import time
list = []

while (True):
    line = input('Enter the command:')
    if (line == 'print'):
        print(list)

    elif (line == 'append'):
        app = input('Enter the text of the element you want to add:')
        list.append(app)
        print('Item added!')
        print()
    elif (line == 'remove'):
        rem = input('Enter the text of the element you want to remove:')
        if rem in list:
            list.remove(rem)
            print('Item removed!')
            print()
        else:
            print('This item is not in the list!')

    elif (line == 'index'):
        ind = int(input('Enter the index of the element you want to remove:'))
        if ind in list:
            del list[ind]
            print('Item removed!')
            print()
        else:
            print('This item is not in the list!')

    elif (line == 'sort'):
        print('In what order should the list be sorted?')
        print('1 - Ascending')
        print('2 - Descending')
        choice = input()
        if choice == '1':
            list.sort()
            print('List sorted!')
            print()
        elif choice == '2':
            list.reverse()
            print('List sorted!')
            print()
        else:
            print('There is no such function!')
    elif (line == 'insert'):
        ins = int(input('Where should I add the element?'))
        app = input('Enter the text of the element you want to add:')
        list.insert(ins, app)
        print('Item added!')
        print()
    elif (line == 'help'):
        print('List of commands:')

        print(''' 1) "append" - Adding an item to the end of the list
2) "remove" - ​​Removing an element by name
3) "index" - Deleting an element by index
4) "sort" - sort the list alphabetically
5) "insert" - Adding an item to a specific place in the list
6) "exit" - Turn off the bot
7) "help" - Displays a list of possible commands ''')
        input('Press enter to exit')
    elif (line == 'exit'):
        print('Shutting down ...')
        time.sleep(2)
        break
    else:
        print('There is no such command! Type "help" to see commands.')
        print()
        time.sleep(1)
