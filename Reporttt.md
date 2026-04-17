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

￼<img width="496" height="40" alt="Image" src="https://github.com/user-attachments/assets/ec9a93a7-c53b-4dbf-9f98-aed27cf4faa8" />
<img width="739" height="31" alt="Image" src="https://github.com/user-attachments/assets/f58e8540-2e75-4e28-8598-1c175fca05f2" />
<img width="577" height="155" alt="Image" src="https://github.com/user-attachments/assets/0229e1f4-6800-4342-be97-0e7173340956" />
<img width="922" height="220" alt="Image" src="https://github.com/user-attachments/assets/508455c5-555b-4851-b8e9-7b0c60781946" />
<img width="470" height="41" alt="Image" src="https://github.com/user-attachments/assets/903e471d-217f-4d2c-a76f-6146c6f6acba" />
<img width="654" height="197" alt="Image" src="https://github.com/user-attachments/assets/3a24fd88-41e3-494c-b383-999170d142a3" />
<img width="687" height="187" alt="Image" src="https://github.com/user-attachments/assets/ac534c6b-3d7c-4449-a129-3bd646c18652" />
<img width="533" height="200" alt="Image" src="https://github.com/user-attachments/assets/53e33e87-aa79-4657-8382-9f70564236c0" />
<img width="670" height="286" alt="Image" src="https://github.com/user-attachments/assets/e2f5e840-755c-4d4e-b3ab-5b1d7e0dab40" />
<img width="457" height="33" alt="Image" src="https://github.com/user-attachments/assets/711a3486-eeb5-4f1b-ab9d-87ad42997065" />
<img width="721" height="87" alt="Image" src="https://github.com/user-attachments/assets/9277af62-5a7b-4dba-88ff-0c870ce9e384" />
<img width="738" height="310" alt="Image" src="https://github.com/user-attachments/assets/2a852a1d-c3fc-4527-b1dc-862c5b595d7c" />
<img width="661" height="91" alt="Image" src="https://github.com/user-attachments/assets/2d172119-b021-43d3-8a31-69f6ba1b666b" />
<img width="306" height="178" alt="Image" src="https://github.com/user-attachments/assets/45e71fec-2009-49cf-814d-f430a2434920" />
<img width="709" height="59" alt="Image" src="https://github.com/user-attachments/assets/a6996f34-5a0c-412d-a3c8-9e2fc7452acb" />
<img width="159" height="82" alt="Image" src="https://github.com/user-attachments/assets/edeec2ef-e492-48d2-879f-f0363d8349f4" />
<img width="597" height="514" alt="Image" src="https://github.com/user-attachments/assets/9f0a9660-b177-496b-acb9-779d47df0484" />
<img width="619" height="141" alt="Image" src="https://github.com/user-attachments/assets/46cd90bf-4d30-4476-9f3c-cbcbaea0a89e" />
<img width="654" height="255" alt="Image" src="https://github.com/user-attachments/assets/a3e7fba4-f67d-414c-85bc-5ab6245bdf27" />

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

Создан файл task_manager.py:
```python
def create_task(title, description):
    # Логика создания задачи
    print(f"Создана новая задача: {title}")
```


