# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.mark.usefixtures("print_time_for_class")
class TestDivision:

    def test_1(self):
        time.sleep(1.5)

    def test_2(self):
        time.sleep(1)

    @pytest.mark.usefixtures("print_time_for_test")
    def test_3(self):
        time.sleep(1.1)


