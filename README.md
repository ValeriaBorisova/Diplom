[![Tests](https://github.com/ValeriaBorisova/Diplom/actions/workflows/main.yml/badge.svg)](https://github.com/ValeriaBorisova/Diplom/actions/workflows/main.yml)

# Diplom
Python

Цель проекта:
```Автоматизация тестирования UI https://berpress.github.io/online-grocery-store/```

В рамках данного проекта были реализованы следующие задачи:

1. Написание автотестов:
* Поиск товаров (негативный и позитивный сценарий)
* Добавление товара в корзину
* Работа с корзиной: удаление/добавление товара и покупка

2. Настройка и запуск тестов в CI
3. Написание тест кейсов
4. Получение отчетов по результатам тестирования

Этапы реализации:

Создаем виртуальное окружение

```python -m venv venv```

Активируем виртуальное окружение

```venv\Scripts\activate.bat``` - для Windows;

```source venv/bin/activate``` - для Linux и MacOS.

Устанока пакетов

```pip install selenium```

```pip install pytest```

```pip install webdriver-manager```

```pip install -r requirements.txt```

pre-commit http://pre-commit.com

```pre-commit run --all-files```

Создание отчетов

```pytest --alluredir=allure-results/```

Установка allure serve https://docs.qameta.io/allure/

Просмотр отчетов

```allure serve allure-results```

Настройка CI реализована через Git Actions

