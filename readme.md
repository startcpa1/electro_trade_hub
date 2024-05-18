## Онлайн платформа торговой сети электроники


### 1. Для запуска приложения требуется настроить виртуальное окружение и установить все зависимости.
    Команда для Windows:
```bash
        - python -m venv venv
        - venv\Scripts\activate
        - pip install -r requirements.txt

    Команда для Unix/Linux:
        - python3 -m venv venv
        - source venv/bin/activate 
        - pip install -r requirements.txt

### 2. Создайте базу данных:

        - psql -U postgres
        - CREATE DATABASE tradehub;
        - \q

### 3. Для заполнения моделей данными необходимо выполнить следующую команду:

    Команда для Windows:
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py loaddata data.json

    Команда для Unix:
        - python manage.py makemigrations
        - python manage.py migrate
        - python3 manage.py loaddata data.json
        
    Внимание: в папке fixtures находятся файлы в формате json по каждому приложению в отдельности. 

### 4. Для работы с переменными окружениями необходимо создать файл .env - пример есть в файле .env_example):

    # Database
    POSTGRES_DB='tradehub'
    POSTGRES_USER='postgres'
    POSTGRES_PASSWORD=/ваш пароль/
    POSTGRES_HOST='127.0.0.1'
    POSTGRES_PORT=/обычно это'5432'/


### 5. Для создания администратора (createsuperuser):

    - заполните поля email, PASSWORD. users/management/commands/csu.py
    Команда для Windows
    - python manage.py csu

    Команда для Unix
    - python3 manage.py csu

### 6. Для запуска приложения:

    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver


### !Внимание!

Доступ к API разрешен только для активных пользователей у кого в профиле стоит галочка активный.
Также если вы являетесь поставщиком, не забудьте поставить галочку в профиле пользователя.

Документация по API находится по адресу: 
- ваш адрес сервера /swagger/
- ваш адрес сервера /redoc/