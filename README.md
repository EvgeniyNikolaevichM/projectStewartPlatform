Описание проекта:
Конструктор масштабируемых роботехнических систем на основе Stewart платформ.

Python >= 3.10
Django >= 4.0
Разработка
1) Активировать виртуальное окружение
venv\Scripts\activate
2Устанавливить зависимости:
 pip install -r requirements.txt
 pip freeze > requirements.txt
3)Выполнить команду для выполнения миграций
 python manage.py makemigrations
 python manage.py migrate
4)Создать суперпользователя
 python manage.py createsuperuser
5)Запустить сервер
 cd StewartPlatformProject
 python manage.py runserver 

Copyright (c) 2021-present, EvgeniyNikolaevich