# Указываем базовый образ
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Устанавливаем зависимости системы  для Linux
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем остальные файлы проекта в контейнер
COPY . .

# Создаем директорию для медиафайлов
RUN mkdir -p /app/media

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]