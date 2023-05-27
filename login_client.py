import requests
import json
import hashlib
import re

def read_email() -> str:
    print(f'(Формат "-----@---.---" )')
    while True:
        inp = input()
        pattern = re.compile('.*@.*\..*')
        if pattern.match(inp):
            return inp
        else:
            print('Что-то не то вы говорите, милсдарь.')

def read(max_int: int) -> int:
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


def registration():
    print('Как вас звать, милсдарь? (Имя)')
    name = input()
    print('Куда вам письма можно слать? (Email)')
    email = read_email()
    print('Придумайте тайное слово. (Пароль)')
    password = input()
    print('Какой вы гильдии?')
    print('1) - Кухарь я (повар)')
    print('2) - Гость я (посетитель)')
    print('3) - Стольник я (официант)')
    role = read(3)

    data = {
        'username': name,
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'role': ['chef', 'customer', 'manager'][role - 1]
    }
    res = requests.post('http://localhost:3000/api/register', json=data)
    print(res.text)
    if res.text == '"ok"':
        print('Записал вас в книгу!')
    else:
        print('Кажется вы уже записаны!')


def login():
    print('Куда вам письма можно слать? (Email)')
    email = read_email()
    print('Скажите тайное слово. (Пароль)')
    password = input()
    data = {
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
    }
    res = requests.post('http://localhost:3000/api/login', json=data)
    if res.text == '"ok"':
        print('Прохрдите, милсдарь! (Успешно)')
    else:
        print('Нет таких в книге! (Неверный логин/пароль)')


while True:
    print('Добро пожаловать, милсдарь! Не признаю я вас что-то.')
    print('1) - Впервые к вам захаживаю (регистрация)')
    print('2) - Я уже бывал здесь. (вход)')
    print('3) -Пшел вон, холоп! (закрыть приложение)')
    print('Чего изволите-c, милсдарь?')

    command = read(3)
    if command == 1:
        registration()
    elif command == 2:
        login()
    else:
        break
