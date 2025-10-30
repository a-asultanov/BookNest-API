# BookNest API

**BookNest API** — это минималистичный REST-сервис на Flask для управления коллекцией книг через HTTP-запросы.  
Приложение поддерживает регистрацию пользователей, JWT-аутентификацию и CRUD-операции с книгами.

---

## Технологии

- Python 3.11+
- Flask — основной веб-фреймворк  
- Flask-SQLAlchemy — ORM для работы с базой данных  
- Flask-Marshmallow — сериализация данных  
- Flask-JWT-Extended — авторизация по токенам  
- SQLite — встроенная база данных  
- python-dotenv — конфигурация окружения  

---

## Возможности

- Регистрация и вход пользователей  
- Авторизация через JWT токены  
- CRUD-операции для книг  
- Проверочный эндпоинт `/api/status`  
- Простая и понятная структура проекта  

---

## Установка и запуск

```bash
# Клонирование проекта
git clone https://github.com/a-asultanov/BookNest-API.git
cd BookNest-API

# Создание и активация виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Создание .env (пример ниже)
cp .env.example .env

# Запуск приложения
python app.py
```

---

## Пример .env

```bash
FLASK_ENV=development
SECRET_KEY=your_flask_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

---

## Примеры запросов

### Регистрация
```
POST /auth/register
```
```json
{
  "username": "arsen",
  "password": "12345"
}
```

### Авторизация (логин)
```
POST /auth/login
```
```json
{
  "username": "arsen",
  "password": "12345"
}
```
**Ответ:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6..."
}
```

### Получить список книг
```
GET /api/books
```
**Headers:**
```
Authorization: Bearer <access_token>
```

### Добавить книгу
```
POST /api/books
```
**Body:**
```json
{
  "title": "Dune",
  "author": "Frank Herbert",
  "genre": "Sci-Fi"
}
```

### Обновить книгу
```
PUT /api/books
```
**Body:**
```json
{
  "id": 1,
  "is_read": true
}
```

### Удалить книгу
```
DELETE /api/books/1
```

---

## Пример ответа API

```json
{
  "id": 1,
  "title": "Dune",
  "author": "Frank Herbert",
  "genre": "Sci-Fi",
  "is_read": false
}
```

---

## Структура проекта

```
booknest_api/
├── app.py
├── config.py
├── extensions.py
├── models.py
├── schemas.py
├── routes.py
├── requirements.txt
└── README.md
```

---

