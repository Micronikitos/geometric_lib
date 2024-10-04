
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`
## Общее описание решения
Проект `geometric_lib` предоставляет функции для работы с геометрическими объектами. Основные функциональные возможности включают вычисление длины и площади окружности,вычисление площади и периметра квадрата.
## Описание функций

### area(r)
**Описание**: Эта функция вычисляет площадь круга по заданному радиусу.
**Пример вызова**:
```cpp
result = area(5)  # Вычисляет площадь круга с радиусом 5
print(result)     # Выведет 78.53981633974483 (приблизительное значение)
```
### perimeter(r)
**Описание**: Эта функция вычисляет длину окружности по заданному радиусу.
**Пример вызова**:
```cpp
result = perimeter(5)  # Вычисляет периметр круга с радиусом 5
print(result)          # Выведет 31.41592653589793
```
### area(a)
**Описание**:Эта функция вычисляет площадь квадрата по заданной стороне.
**Пример вызова**:
```cpp
result = area(4)  # Вычисляет площадь квадрата со стороной 4
print(result)     # Выведет 16
```
### perimeter(a)
**Описание**: Эта функция вычисляет периметр квадрата по заданной стороне.
**Пример вызова**:
```cpp
result = perimeter(4)  # Вычисляет периметр квадрата со стороной 4
print(result)          # Выведет 16
```
## История изменений
- Commit `604901a443221b40e6ace37c11d17f7926afb821`: Добавил кометарии к circle.py.
- Commit `fa1db11ef45bb3f451c6491287a4cf6789e80815`: Добавил кометарии к square.py.


