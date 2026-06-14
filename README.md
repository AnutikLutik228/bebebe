# 🐳 Docker Mountains Project

Проект для генерации данных о горах и создания HTML-отчёта с использованием Docker.

---

# 📁 Структура проекта

```text
HW3/
│
├── data/
│   ├── data.csv
│   └── report.html
│
├── generator/
│   ├── Dockerfile
│   └── generate.py
│
├── reporter/
│   ├── Dockerfile
│   └── report.py
│
├── local_data/
│
├── run.sh
└── README.md
```

# 🏔 Генератор данных

Генератор создаёт CSV-файл со случайными данными о горах.

Поля:

- id
- mountain
- country
- height
- difficulty

Пример данных:

```csv
1,Everest,Nepal,8848,hard
2,Elbrus,Russia,5642,medium
```

---

# 📄 HTML отчёт

Контейнер аналитика читает CSV-файл и создаёт HTML-таблицу.

После запуска появляется файл:

```text
data/report.html
```

---

# 🚀 Команды проекта

## Показать структуру проекта

```bash
./run.sh structure
```

## Собрать контейнер генератора

```bash
./run.sh build_generator
```

## Запустить генератор

```bash
./run.sh run_generator
```

## Собрать контейнер аналитика

```bash
./run.sh build_reporter
```

## Создать HTML отчёт

```bash
./run.sh run_reporter
```

---

# 🌐 Просмотр отчёта

```bash
open data/report.html
```

---

# 📦 Docker volumes

В проекте используется volume:

```text
$(pwd)/data:/app/data
```

Это позволяет контейнерам работать с локальными файлами проекта.

---

# ✅ Результат работы

Проект:

- генерирует CSV-файл;
- создаёт HTML-отчёт;
- использует Docker-контейнеры;
- управляется через `run.sh`.

---
Орлова Анна Андреевна ББИ2510