# Платформа курсов (монорепозиторий)

Монорепозиторий курса: сервисы, инфраструктура, документация и учебный сервис заметок.

**Стек:** Python · FastAPI · Docker · pre-commit

## Структура

- `services/` — микросервисы (каждый сервис — отдельный модуль)
- `infra/` — инфраструктура (gateway, monitoring)
- `compose/` — сборки окружений (dev/prod)
- `docs/` — документация курса и проекта
- `fastapi_lesson/` — учебный сервис заметок на FastAPI
- `python-version-guide.md` — инструкция по смене версии Python в Windows

## Базовые правила

- Все изменения — через pull request
- Каждый сервис имеет `/health` и `/version`
- Конфигурация — через env

## Запуск учебного сервиса

```bash
pip install -r requirements.txt
uvicorn fastapi_lesson.app:app --reload
```
