# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
from contextlib import nullcontext as does_not_raise


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("nom, denom, result, expectation",
                         [pytest.param(10, 2, 5, does_not_raise(), marks=pytest.mark.smoke),
                          pytest.param(10, 25, 0.4, does_not_raise(), marks=pytest.mark.skip),
                          (10, -7, -10 / 7, does_not_raise()),
                          (10, '0', 1, pytest.raises(TypeError)),
                          (10, 0, 1, pytest.raises(ZeroDivisionError))])
def test_all_division(nom, denom, result, expectation):
    with expectation:
        assert all_division(nom, denom) == result
