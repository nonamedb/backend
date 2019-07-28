# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import json
import requests
import pytest
import django

django.setup()


URL = 'http://83.220.170.234:8080'
# URL = 'http://localhost:8080'

#
# def test_predictor_get():
#     res = requests.get('{}/{}/'.format(URL, 'prediction'))
#     print(res.json())


@pytest.mark.parametrize("students_data", [
    # json.dumps([{'developer': 50}, {'tutor': 40}, {'lawyer': 60}, {'cook': 10}, {'painter': 20}]),
    # json.dumps([{'developer': 55}, {'tutor': 20}, {'lawyer': 40}, {'cook': 30}, {'painter': 10}]),
    json.dumps([{'developer': 20}, {'tutor': 40}, {'lawyer': 60}, {'cook': 10}, {'painter': 20}, {'hostel': 25}])
])
def test_predictor_post(students_data):
    res = requests.post('{}/{}/'.format(URL, 'prediction'), data={'data': students_data})
    print(res.json())
    assert True
