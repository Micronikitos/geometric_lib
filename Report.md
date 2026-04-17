# Лабораторная работа №5: Git Advanced Workshop

---

## Цель работы

Освоение продвинутых техник работы с Git: ветвление, разрешение конфликтов, использование Git Hooks для автоматизации и управление проектом с помощью Git Flow.

---

## 1. Создание и клонирование репозитория

Был создан репозиторий `git-practice` на GitHub и клонирован на локальную машину.

```bash
git clone https://github.com/Micronikitos/git-practice.git
cd git-practice
```

￼

￼

---

##  2. Первый коммит и создание структуры книги
Создан файл book.md с начальной структурой книги и отправлен на GitHub.

```bash
echo "# Название книги" > book.md
echo "" >> book.md
echo "## Глава 1: Введение" >> book.md
echo "Здесь будет введение в тему книги." >> book.md
echo "" >> book.md
echo "## Глава 2: Основы Git" >> book.md
echo "Основные понятия и команды Git." >> book.md
git add book.md
git commit -m "File added book.md"
git push origin main
```

￼

￼

---

##  3. Работа с ветками
Создание ветки feature-login
```bash
git checkout -b feature-login
git branch
```

￼
## Добавление главы 3 в ветке feature-login
Файл book.md дополнен главой 3:
# Название книги

## Глава 1: Введение
Здесь будет введение в тему книги.

## Глава 2: Основы Git
Основные понятия и команды Git.

## Глава 3: Вход в систему
Раздел по новой функциональности входа в систему.
```bash
git add book.md
git commit -m "Добавлена глава 3: Вход в систему"
git push origin feature-login
```

Создание фичи task-management
```python
brew install git-flow
git flow init -d
```


