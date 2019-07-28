# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import requests
import pytest
import django

django.setup()


URL = 'http://83.220.170.234:8080'


def test_predictor_get():
    res = requests.get('{}/{}/'.format(URL, 'prediction'))
    print(res.json())


@pytest.mark.skip
@pytest.mark.parametrize("spec,year,labor_coef,released_coef,delta_industry", [
    ('developer', 2021, 0.2, 0.9, 0.1),
    ('tutor', 2023, 0.2, 0.9, 0.5),
    ('lawyer', 2024, 0.2, 0.9, 0.3),
    ('cook', 2025, 0.2, 0.9, 0.2),
    ('painter', 2025, 0.2, 0.9, 0.2)
])
def test_predictor_post(spec, year, labor_coef, released_coef, delta_industry):
    res = requests.get('{}/{}/'.format(URL, 'prediction'), spec=spec, year=year, labor_coef=labor_coef, released_coef=released_coef, delta_industry=delta_industry)
    print(res)
    assert True
