# Задание № 4 «Система обработки заказов ресторана»
## Фирсов Федор БПИ219.

Разработаны 2 микросервиса с общим сервером:
1. [Код клиента для регистрации/входа](https://github.com/fodof91/Harchevnya/blob/master/LoginClient.py)
2. [Код клиента для управления заказами](https://github.com/fodof91/Harchevnya/blob/master/OrderClient.py)
3. [Код сервера](https://github.com/fodof91/Harchevnya/blob/master/server.py)



### Микросервис авторизации пользователей
При выходе информация о пользователе сохраняется в локальный файл. -> сохраняется при повторном входе.
Наглядный пример работы:
![alt text](https://github.com/fodof91/Harchevnya/blob/master/img/reg.png)
![alt text](https://github.com/fodof91/Harchevnya/blob/master/img/log.png)
### Микросервис обработки заказов
Реализован весе необходимые функции.
Наглядный пример работы:
![alt text](https://github.com/fodof91/Harchevnya/blob/master/img/guest.png)
![alt text](https://github.com/fodof91/Harchevnya/blob/master/img/chef.png)
![alt text](https://github.com/fodof91/Harchevnya/blob/master/img/stol.png)

### БД
Я использовал MySQL базу данных подняьтую на localhost:3306 и database cooker. 

### Документация
Во всех функция расстаылены комментарии и TypeHint-ы
