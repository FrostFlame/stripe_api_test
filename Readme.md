# Тестовое задание
Тестовое задание, простой сервер с парой html страниц, который позволяет
"оплачивать" отдельные товары и заказы, из них состоящие, с помощью api
платёжной системы stripe.

## Содержание
- [Установка зависимостей](#установка-зависимостей)
- [Запуск сервера](#запуск-сервера)
- [API](#api)
- [Удалённый сервер](#удалённый-сервер)
- [Команда проекта](#команда-проекта)


## Использование
Создайте .env файл по образцу .env.example


### Установка зависимостей
Для установки зависимостей, выполните команду:
```
$ pip install -r requirements.txt
```

### Запуск сервера
Чтобы запустить сервер, выполните команду:
```
$ python manage.py runserver
```


### API
- [/](https://strpiapi.herokuapp.com/) - Корень проекта
- [/items](https://strpiapi.herokuapp.com/items) - drf страница списка всех Items
- [/items/{id}]() - drf страница Item
- [/orders](https://strpiapi.herokuapp.com/orders) - drf страница списка всех Orders
- [/orders/{id}]() - drf страница Order
- [/discounts](https://strpiapi.herokuapp.com/discounts) - drf страница списка всех Discount
- [/discounts/{id}]() - drf страница Discount
- [/taxes](https://strpiapi.herokuapp.com/taxes) - drf страница списка всех Taxes
- [/taxes/{id}]() - drf страница Tax
- [/buy/{id}]() - получение Stripe Session Id для оплаты выбранного Item
- [/item/{id}]() - получение html страницы выбранного Item
- [/order_bulk/{id}]() - получение Stripe Session Id для оплаты выбранного Order
- [/order/{id}]() - получение html страницы выбранного Order


### Удалённый сервер
Приложение развёрнуто на heroku.
Ссылка - [https://strpiapi.herokuapp.com/](https://strpiapi.herokuapp.com/)
Некоторые ссылки в пункте [API](#api) также ведут на этот сервер.


### Команда проекта

- [Серазетдинов Дамир](https://t.me/serazetdinov)
 