#!/bin/bash

echo "Ожидаем запуска базы данных..."
sleep 7

cd src

echo "Создание и применение миграций..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Создание суперпользователя"
python manage.py createsuperuser --noinput --username admin --email admin@example.com

echo "Запуск приложения..."
gunicorn config.wsgi --bind 0.0.0.0:8000
