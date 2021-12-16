Описание проекта:
Конструктор масштабируемых роботехнических систем на основе Stewart платформ.

Инструменты разработки
Стек:

Python >= 3.10
Django >= 4.0
sqlite3
Разработка
1) Создать виртуальное окружение
python -m venv venv
2)Активировать виртуальное окружение
venv\Scripts\activate
2) Устанавливить зависимости:
 pip install -r requirements.txt
 pip freeze > requirements.txt
3) Выполнить команду для выполнения миграций
python manage.py migrate
4) Создать суперпользователя
python manage.py createsuperuser
5) Запустить сервер
python manage.py runserver

Copyright (c) 2021-present, EvgeniyNikolaevich