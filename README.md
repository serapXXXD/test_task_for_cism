# Тестовое задания для ЦИСМ
## Установка через Docker

### У вас должен быть установлен и запущен Docker



Скопируйте проект командой 
 ```bash
git clone git@github.com:serapXXXD/test_task_for_cism.git
 ```
Перейдите в 
 ```bash
cd cism_infra
 ```
Создайте .env файл
 ```bash
touch .env
 ```

Получите новый ключ джанго 
https://djecrety.ir/

Формат ключа:

django-insecure-```jvlf+slausy7o2#ak^%yji@p*g7lx(rxy4m23v1%+kwic_6ign```

Вам нужно заполнить .env по примеру

 ```bash
SECRET_KEY=django-insecure-jvlf+slausy7o2#ak^%yji@p*g7lx(rxy4m23v1%+kwic_6ign
DEBUG=0

POSTGRES_ENGINE='django.db.backends.postgresql_psycopg2' # не менять
POSTGRES_NAME=cism
POSTGRES_USER=cism
POSTGRES_PASSWORD=posgres
POSTGRES_HOST=data_base
POSTGRES_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost

PAGE_SIZE_IN_API=5
 ```

Пояснения:
 ```bash
До и после занка "=" пробелов быть не должно!

DEBUG=1 дебаг включен | 0 дебаг выключен

PAGE_SIZE_IN_API=5 количество объектов отоброжаемых на 1 странице в API

В параметре "ALLOWED_HOSTS" укажите список хостов слитно через запятую
 ```

Запускаем docker-compose

 ```bash
docker-compose up --build -d
 ```

 ```bash
docker ps
 ```

Должно быть запущенно 3 контейнера
 ```bash
NAMES
cism_infra_nginx_1
cism_infra_backend_1
cism_infra_data_base_1
 ```

Далее нужно провалиться в образ с бэкэндом
 ```bash
docker exec -it blog_infra_backend_1 sh
 ```

Примичание !
в данной сборке для работы с регистрацией и авторизацией пользователей используется 

```djoser==2.2.2 ```

докементация по djoser
https://djoser.readthedocs.io/en/latest/getting_started.html

Создайте 1 или несколько супер пользователей
 ```bash
python manage.py createsuperuser
 ```

Заполните требуемые поля

Выходим из образа
 ```bash
exit
 ```

Для получения токена авторизации перейдите по адресу 
http://127.0.0.1/api/v1/auth/token/login/

Для получения списка постов и работы с ними перейдите по адресу 
http://127.0.0.1/api/v1/posts/

Для работы с конкретным постом перейдите по адресу 
http://127.0.0.1/api/v1/posts/ <номер (id) поста>