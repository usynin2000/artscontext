# Используем официальный образ Python 3.10.6 в качестве базового
FROM python:3.10.6-slim

# Устанавливаем переменную окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED=1

# Обновляем пакеты и устанавливаем gcc и другие зависимости для компиляции
RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . /app/

# Указываем команду для запуска вашего приложения
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8888"]
