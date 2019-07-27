# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import pytest
import django

django.setup()

from layer_business.calculator import VacanciesCalculatorBL


def setup():
    pass


@pytest.mark.run(order=0)
@pytest.mark.parametrize("spec,year", [
    ('developer', 2021, 'labor_coef', 'released_coef', 'delta_industry')
])
def test_vacancies_calculator(spec, year, labor_coef, released_coef, delta_industry):
    calculator = VacanciesCalculatorBL()
    calc_result = calculator.calculate(spec, year, labor_coef=labor_coef, released_coef=released_coef, delta_industry=delta_industry)
    print(calc_result)
    assert True
