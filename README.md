# 🐳 HW3 Docker Project

## 📌 Описание проекта

Проект состоит из двух Docker контейнеров:

* **generator** — генерирует CSV файл с данными о горах
* **reporter** — создает HTML отчет на основе CSV файла

Контейнеры взаимодействуют через общую папку `data`, подключенную с помощью Docker volume.

---

## 📂 Структура проекта

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
├── run.sh
├── README.md
└── .gitignore
```



## 🚀 Команды проекта

### Сборка контейнера генератора

```bash
./run.sh build_generator
```

### Запуск генератора данных

```bash
./run.sh run_generator
```

После запуска создается файл:

```text
data/data.csv
```

---

### Очистка папки data

```bash
./run.sh clear_data
```

---

### Просмотр структуры проекта

```bash
./run.sh structure
```

---

## 📊 Генерация HTML отчета

Сборка reporter контейнера:

```bash
docker build -t reporter-image ./reporter
```

Запуск reporter контейнера:

```bash
docker run --rm -v "$(pwd)/data:/app/data" reporter-image
```

После запуска создается файл:

```text
data/report.html
```

---

## 🌋 Пример данных

| Mountain | Country | Height |
| -------- | ------- | ------ |
| Everest  | Nepal   | 8848   |
| Elbrus   | Russia  | 5642   |
| Denali   | USA     | 6190   |

---

## ✨ Результат работы

Проект автоматически:

1. Генерирует CSV файл с данными
2. Создает HTML таблицу
3. Сохраняет результат в общую папку `data`
4. Использует Docker volume для обмена данными между контейнерами

---

