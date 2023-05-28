import re

# read string from string in email format
def read_email() -> str:
    print(f'(Формат "-----@---.---" )')
    while True:
        inp = input()
        pattern = re.compile('.*@.*\..*')
        if pattern.match(inp):
            return inp
        else:
            print('Что-то не то вы говорите, милсдарь.')


# read number from 1 to max_int (user command)
def read_command(max_int: int) -> int:
    print(f'(Введите число от 1 до {max_int})')
    while True:
        try:
            inp = int(input())
            if inp < 1 or inp > max_int:
                raise Exception
            return inp
        except:
            print('Что-то не понимаю я вас, милсдарь.')
            print(f'(Введите число от 1 до {max_int})')
