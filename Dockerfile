# Используем Python-образ
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости в рабочую директорию
COPY requirements.txt .

# устанавливаем зависимости без кеширования для уменьшения контейнера
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

# Запускаем бота
CMD ["python", "bot/main.py"]