import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def print_time_for_class():
    yield print(f'Время начала выполнения класса с тестами: {datetime.now().time()}')
    print(f'\nВремя окончания выполнения класса с тестами: {datetime.now().time()}')


@pytest.fixture
def print_time_for_test():
    start_time = datetime.now()
    yield start_time
    end_time = datetime.now()
    print(f'Время выполнения теста:{end_time - start_time}')
