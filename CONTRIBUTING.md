# Contributing

## Как сдаём задания
1. Создаём ветку от main:
   git checkout -b feat/<task-name>

2. Вносим изменения и проверяем запуск

3. Делаем осмысленные коммиты:
   feat: ...
   fix: ...
   docs: ...
   chore: ...

4. Открываем Pull Request в main

## Стандарты сервисов
Каждый сервис обязан иметь:
- /health
- /version
- Dockerfile
- .env.example
- README.md

## Запрещено
- Пушить .env и секреты
- Работать напрямую в main
