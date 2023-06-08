# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    """
    Проверка деления целочисленных чисел с результатом = целое число
    """
    assert all_division(6, 3) == 2


def test22():
    """
    Проверка деления целочисленных чисел с результатом = дробное число
    """
    assert all_division(3, 6) == 0.5


def test23():
    """
    Проверка деления числа на само себя
    """
    assert all_division(5, 5) == 1


@pytest.mark.smoke
def test4():
    """
    Проверка деления 0 на число
    """
    assert all_division(0, 1) == 0


def test5():
    """
    Проверка деления числа на 0
    """
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)
