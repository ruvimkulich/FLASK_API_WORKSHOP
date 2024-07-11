# Twit_API
API предоставляющее возможность ведения блога.

<!--Установка-->
## Установка (Windows)

1. Клонирование репозитория 

```git clone git@github.com:ruvimkulich/Twit_API.git```

2. Переход в директорию Twit_API

```cd Twit_API```

3. Создание виртуального окружения

```python -m venv venv```

4. Активация виртуального окружения

```venv\Scripts\activate.bat```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Запуск приложения

```python main.py```


<!--Тестирование-->
## Тестирование

Тестирование в Postman

Создать новую колекцию запросов и сами запросы. Запрос должен включать в себя метод, URL, тело (для метода POST и PUT).

- Получение всех твитов:
  - Метод: GET 
  - URL: localhost:5000/twit

- Получение твита по id:
  - Метод: GET
  - URL: localhost:5000/twit/<twit_id>

- Создание нового твита: 
  - Метод: POST
  - URL: localhost:5000/twit
  - Тело запроса: {"body": "Hello World", "author": "@aqaguy"}

- Редактирование твита:
  - Метод: PUT 
  - URL: localhost:5000/twit/<twit_id>
  - Тело запроса: {"body": "Bye World", "author": "@aqaguy"}

- Удаление твита: 
  - Метод: DELETE
  - URL: localhost:5000/twit/<twit_id>


<twit_id> автоматически генерируется во время создания нового твита.