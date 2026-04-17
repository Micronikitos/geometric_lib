# Лабораторная работа №5: Git Advanced Workshop

**Студент:** [Ваше ФИО]
**Группа:** [Ваша группа]
**Дата:** [Дата выполнения]

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
