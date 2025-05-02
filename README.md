# Online Store

Онлайн-магазин, разработанный на Django, с минимальным frontend-интерфейсом и гибкой backend-архитектурой.

## 🔧 Возможности
- Каталог товаров с фильтрацией
- Админка Django для управления заказами
- Авторизация пользователей
- Корзина и оформление заказа (в процессе)

## 🚀 Технологии
- Django
- SQLite (или PostgreSQL)
- Bootstrap / Tailwind (планируется)

## 📦 Установка
```bash
git clone https://github.com/XikoSan/online_store.git
cd online_store
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
