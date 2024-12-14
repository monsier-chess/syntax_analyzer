print('''
73. Выражения значений функции t(x)=2*x в единичной системе счисления
    Правильные записи: s(1)=11; s(11)=1111; s(111)=111111

Дополнительные примеры:
    1. t(111)=1111111
    2. s(1111)=11111111
Некорректные выражения:
    1. z(1) = 11
    2. s(11)=111
    3. s ( 1 1 ) = 1 1 1 1

''')

input_string = input('Введите строку: ')
current_index = 0
ch = None


def readch():
    global ch, current_index
    if current_index < len(input_string):
        ch = input_string[current_index]
        current_index += 1
    else:
        ch = None


class ParsingError(ValueError):
    def __init__(self, message):
        super().__init__(message)


def error():
    raise ParsingError('Некорректный ввод')


def vyrazhenie():
    oboznachenie_funkcii()
    if ch == '(':
        readch()
    else:
        error()
    ostavshayasya_chast()


def oboznachenie_funkcii():
    if ch in {'s'}:
        if ch == 's':
            readch()
        else:
            error()
        return
    if ch in {'t'}:
        if ch == 't':
            readch()
        else:
            error()
        return
    error()


def ostavshayasya_chast():
    if ch == '1':
        readch()
    else:
        error()
    center()
    if ch == '1':
        readch()
    else:
        error()
    if ch == '1':
        readch()
    else:
        error()
    return


def center():
    if ch in {'1'}:
        if ch == '1':
            readch()
        else:
            error()
        center()
        if ch == '1':
            readch()
        else:
            error()
        if ch == '1':
            readch()
        else:
            error()
        return
    if ch in {')'}:
        if ch == ')':
            readch()
        else:
            error()
        if ch == '=':
            readch()
        else:
            error()
        return
    error()


while True:
    readch()
    try:
        vyrazhenie()
        if ch is None:
            print('Успешно!')
        else:
            error()
    except ParsingError as err:
        print(err)
    want_continue = input(
        'Хотите ввести другое выражение? ("Да" если хотите продолжить, иначе - выход): '
    )
    want_continue = want_continue.lower().strip()
    if want_continue != 'да':
        print('Завершение работы программы')
        break
    input_string = input('Введите строку: ')
    current_index = 0
    ch = None
