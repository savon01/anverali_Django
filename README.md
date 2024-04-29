# Простой сайт с админ панелью и двумя кабинетами на Django


## Установка

1. Клонируйте репозиторий:

   ```shell
   git clone https://github.com/savon01/anverali_Django.git
    ```
2. Перейдите в директорию проекта:
    ```shell
   cd mysite
    ```
3. Установите зависимости:
    ```shell
   pip install -r requirements.txt
    ```
4. Установите PostgreSQL на вашем сервере и настройте его. Вы можете найти инструкции для установки и настройки PostgreSQL в соответствии с вашей операционной системой на официальном сайте PostgreSQL.
5. В файле settings.py вашего Django-проекта обновите настройки базы данных, чтобы использовать PostgreSQL вместо текущей базы данных. Вот пример настроек для PostgreSQL:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
необходимо заменить на свои данные

6. Создайте базу данных PostgreSQL с помощью команды Django:
    ```shell
   python manage.py migrate
    ```
7. Если не создаться таблица Profile, введите следующие команды: 
    ```shell
   python manage.py migrate mysite
    ```
    ```shell
   python manage.py makemigrations
    ```
8. Создайте администратора сайта:
    ```shell
   python manage.py createsuperuser
    ```
и следуй инструкции в терминале
# Использование
1. Запустите приложение:
    ```shell
   python manage.py runserver
    ```
2. Откройте приложение в браузере:
    ```shell
   http://localhost:8000
    ```
3. Админка доступна по адресу: 
    ```shell
   http://localhost:8000/admin
    ```