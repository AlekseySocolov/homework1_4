def question (yearbirth, date, name):
    year_of_birth = input(f'Введеите год рождения {name}: ')
    if year_of_birth == yearbirth:
        birthday = input(f'Введеите день рождения {name}: ')
        if birthday == date:
            print('Верно')
        else:
            print('Неверный день рождения')
    else:
        print('Неверный год рождения')


Yearbirth = '1799'
Date = '6'
Name = 'А.С Пушкина'

question (Yearbirth, Date, Name)
question ('1799', '6', 'А.С Пушкина')