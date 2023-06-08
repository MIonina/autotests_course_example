# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures('start_end_stop')
class TestDivision:
    def all_division(*arg1):
        division = arg1[1]
        for i in arg1[2:]:
            division /= i
        return division

    def test1(self):
        assert self.all_division(6, 3) == 2

    def test2(self):
        assert self.all_division(3, 6) == 0.5

    def test3(self):
        assert self.all_division(5, 5) == 1

    def test4(self):
        assert self.all_division(0, 1) == 0

    def test5(self, time):
        with pytest.raises(ZeroDivisionError):
            self.all_division(1, 0)

