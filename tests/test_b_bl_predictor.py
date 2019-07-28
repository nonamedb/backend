# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import pytest
import django

django.setup()

from layer_business.predictor import PredictorBL


@pytest.mark.run(order=0)
@pytest.mark.parametrize("spec,year", [
    ('hostel', 2019)
])
def test_predictor(spec, year):
    calculator = PredictorBL()
    calc_result = calculator.calculate(spec, year)
    print(calc_result)
    assert True
