Курсовая работа: Трекер полезных привычек

Контекст:
В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.


Для запуска проекта требуется:
- Создать виртуальное окружение
- Установить зависимости из файла requirements.txt
- создать БД
- Создать суперюзера python3 manage.py csu
- Выполнить миграции
- запустить проект

Для запуска переодических задач требуется выполнить команды:
 - celery -A config beat -l info -S django
 - celery -A config worker -l INFO

Версия Python: 3.11.14
Версия Django: 4.2.5
Полный список модулей содержится в файле requirements.txt

Созданы контейнеры для Docker
Для запуска Docker использовать комманды:
 - docker compose build
 - docker compose up
Выполнить миграции:
 - docker compose exec app python manage.py migrate