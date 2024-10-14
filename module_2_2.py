              # первый вариант решения
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if (first == second) and (second == third):
    print(3)
elif (first != second) and (second != third) and (first != third):
    print(0)
else:
    print(2)

             # второй вариант решения с использованием мощности множества
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
set_ = {first, second, third}
if len(set_) == 1:
    print(3)
elif len(set_) == 2:
    print(2)
else:
    print(0)