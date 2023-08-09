# Алгоритм быстрой сортировки.
# Написать функцию, которая реализует алгоритм "Быстрой сортировки".
# Вводятся следующие параметры:
# - количество значений (с использованием конструкции try-except)
# - ввод чисел с клавиатуры (в список) (с использованием конструкции try-except)


try:
    lenList = int(input('Введите количество элементов списка: '))
    someList = []

    try:
        for index in range(lenList):
            someList.append(int(input()))
        print(someList)
        print(sorted(someList))

    except ValueError:
        print('Все элементы списка должны быть числами!')

except ValueError:
    print('Это не число!')

finally:
    print('Выполнение программы завершено')




# # Пример с урока:
# try:
#     number1 = int(input('Enter a number: '))
#     number2 = int(input('Enter another number: '))
#     result = number1 / number2
#     print(result)
# except ZeroDivisionError:
#     print('You can not divide by zero!')
#
# except Exception as e:
#     print(f'Информация об ошибке - {e}')

# finally:
#     print('Выполнение программы завершено')



