import json

import requests
import hashlib

from Utils import read_command, read_email

# create request to server to create new user
def registration() -> None:
    print('Как вас звать, милсдарь? (Имя)')
    name = input()
    print('Куда вам письма можно слать? (Email)')
    email = read_email()
    print('Придумайте тайное слово. (Пароль)')
    password = input()
    print('Какой вы гильдии?')
    print('1) - Кухарь я (повар)')
    print('2) - Гость я (посетитель)')
    print('3) - Стольник я (менеджер)')
    role = read_command(3)

    data = {
        'username': name,
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'role': ['chef', 'customer', 'manager'][role - 1]
    }
    res = requests.post('http://localhost:3000/api/register', json=data)
    if res.status_code == 200:
        print('Записал вас в книгу!')
    elif res.status_code == 409:
        print('Кажется вы уже записаны!')
    else:
        print('Непредвиденные трудности!')


# create request to server to login user
def login() -> None:
    print('Куда вам письма можно слать? (Email)')
    email = read_email()
    print('Скажите тайное слово. (Пароль)')
    password = input()
    data = {
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
    }
    res = requests.post('http://localhost:3000/api/login', json=data)
    if res.status_code == 200:
        print('Нашел вас в книге, милсдарь! (Успешно)')
        info_file = open('info.txt', 'w')
        print(res.text, file=info_file)
        info_file.close()
    elif res.status_code == 409:
        print('Нет таких в книге! (Неверный логин/пароль)')
    else:
        print('Непредвиденные трудности!')


# create request to server to get info about user
def info():
    try:
        info_file = open('info.txt')
        session_id = int(info_file.read())
        info_file.close()
        data = {
            'session_id': session_id,
        }
        res = requests.post('http://localhost:3000/api/session', json=data)
        if res.status_code == 200:
            res = json.loads(res.text)
            print(f'Проходите, милсдарь {res["role"]} {res["name"]}! (Успешно)')
        elif res.status_code == 409:
            print('Не припомню вас! (Cессия закончилась)')
        elif res.status_code == 404:
            print('Не видал вас раньше! (Не выполнен вход)')
        else:
            print('Непредвиденные трудности!')
    except:
        print('Не видал вас раньше! (Не выполнен вход)')


# client main function
def main():
    while True:
        print('Добро пожаловать, милсдарь! Чего изволите.')
        print('1) - Впервые к вам захаживаю (регистрация)')
        print('2) - Я уже бывал здесь. (вход)')
        print('3) - Узнаешь меня? (Информация о пользователе.)')
        print('4) -Пшел вон, холоп! (закрыть приложение)')
        print('Чего изволите-c, милсдарь?')

        command = read_command(4)
        if command == 1:
            registration()
        elif command == 2:
            login()
        elif command == 3:
            info()
        else:
            break

main()
