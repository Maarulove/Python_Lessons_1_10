from script import input_data, print_data, delete_data, edit_data


def interface():
    print('Доброго времени суток! Вы попали на специальную программу от нашей группы! Что же мы можем делать?\n'
          '1. Записать данные(в 2-ух форматах)\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    command = int(input("Введите номер операции: "))
    
    while command < 1 or command > 4:
        print('Попробуйте ещё раз выбрать правильную команду')
        command = int(input("Введите номер операции: "))
        
    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        edit_data()
    else:
        print_data()