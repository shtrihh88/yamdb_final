# REST API Yamdb

***
![example workflow](https://github.com/shtrihh88/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

***

# API YaMDb
Учебный проект Яндекс Практикум, создан с помощью `django` и 
`django-rest-framework` с использованием postgresql в качестве
базы данных. Запуск возможен с помощью `docker`.

Проект YaMDb - это сервис собирающий отзывы пользователей
на книги, фильмы, музыку. Список категорий может быть расширен
администратором сервиса. У произведения есть жанр,
который можно выбрать из списка предустановленных
(например, «Сказка», «Детектив» и т.п).
Жанры создаются администратором сервиса.
Пользователи могут оставить свой отзыв на произведение,
но не более одного раза.

***

## Установка проекта на локальном компьютере

***

### 1. Подготовить docker согласно официальной [инструкции](https://docs.docker.com/engine/install/).

### 2.Клонировать репозиторий, перейти в папку проекта.
```
git clone https://github.com/shtrihh88/yamdb_final
cd yamdb_final
```

### 3.В корне проекта создать файл .env.
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль>
DB_HOST=db
DB_PORT=5432
```

### 4.Запустить проект, создать и применить миграции, собрать статику.
```
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input
```

***

## Документация и панель администратора.
Документация API находится по адресу:
```
127.0.0.1/redoc
```
Панель администратора:
```
127.0.0.1/admin
```

***

## Основные использованные технологии
* python 3.8
* [django](https://www.djangoproject.com/)
* [drf](https://www.django-rest-framework.org/)
* [posgresql](https://www.postgresql.org/)
* [docker](https://www.docker.com/)

***

### Ссылка на DockerHub:
https://hub.docker.com/repository/docker/shtrihh88/api_yamdb_final

### Об авторе
Громов Александр, github.com/shtrihh88, shtrihh88@gmail.com
