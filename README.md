# Трекер привычек

Бэкенд-часть веб-приложения для формирования привычек, вдохновленная книгой Джеймса Клира
«Атомные привычки». 
Отправляет напоминание о выполнении привычки с помощью Telegram-бота.


## Содержание
- Установка
- Использование
- Тестирование
- Документация


## Установка
**Клонирование репозитория на локальный репозиторий:**
1. Чтобы клонировать репозиторий с GitHub себе на компьютер, необходимо
получить ссылку на доступ к репозиторию в разделе **Code** на странице
репозитория, выбрать способ взаимодействия с GitHub (**HTTPS**) и **скопировать**
ссылку на репозиторий для клонирования.
2. В главном меню **PyCharm** перейдите в меню **Get from VCS**. 
3. Вставьте ссылку на репозиторий и нажмите на кнопку **Clone**.
4. По окончании клонирования будет открыт проект, вы можете работать с этим проектом.

Или выполните команду ```git clone <ссылка_на_репозиторий>``` 

**Установка зависимостей:** ```poetry install```

**Создайте базу данных и выполните миграции:** ```python manage.py migrate```


## Использование

**Запустите локальный сервер:** ```python manage.py runserver```

**Запустите celery worker:** ```celery -A config worker -l INFO -P```

**Запустите celery beat:** ```celery -A config beat```

**Запустите сервер redis**

**Запустите кастомную команду runtelegrambot:** ```python manage.py runtelegrambot```

**Общий алгоритм работы с приложением:**
1. Создать пользователя. 
2. В ответе запроса на регистрацию будет ссылка на Telegram-бота. 
3. Написать боту /start и подтвердить почту. 
4. Получить токен доступа для созданного пользователя для дальнейшей работы. 
5. Создать привычки, приятные привычки и вознаграждения.

После этого бот будет присылать уведомления о необходимости выполнить привычку.

**Доступные эндпоинты:**
- habit_tracker/habit_create/ - создание привычки
- habit_tracker/habit_list/ - список привычек пользователя
- habit_tracker/habit_list/public/ - список публичных привычек
- habit_tracker/habit_retrieve/habit_id/ - детали конкретной привычки
- habit_tracker/habit_update/habit_id/ - обновление привычки
- habit_tracker/habit_delete/habit_id/ - удаление привычки
- users/token/ - получение токена авторизации
- users/token_refresh/ - обновление токена авторизации
- users/user_register/ - создание пользователя
- users/user_profile/user_id/ - профиль текущего пользователя
- users/user_profile/update/user_id/ - обновление профиля пользователя
- users/user_profile/delete/user_id/ - удаление профиля пользователя
- api/docs/ - документация Swagger
- api/docs/redoc/ - документация Redoc

Эндпоинты создания пользователя и получения токена открыты для 
неавторизованных пользователей. Остальные эндпоинты закрыты авторизацией, 
а так же имеют другие ограничения.


## Тестирование
Тесты находятся в каждом приложении в директории tests. Вы можете выполнить
проверку, выполнив команду ```python manage.py test```, и проверить покрытие
кода тестами с помощью команды ```coverage run manage.py test```.


## Документация
Документацию можно посмотреть по эндпинтам: 
```api/docs/``` или ```api/docs/redoc/```.
