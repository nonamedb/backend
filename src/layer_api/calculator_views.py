# coding: utf-8


import json
from django.http import JsonResponse
from leon_base.base.views import BaseView
from layer_business.calculator import VacanciesCalculatorBL


class CalculatorValidatorMixin:

    @staticmethod
    def _spec_validator(value, default):
        return value if value else default

    @staticmethod
    def _year_validator(value, default):
        return int(value) if value else default

    @staticmethod
    def _labor_coef_validator(value, default):
        return float(value) if value else default

    @staticmethod
    def _delta_industry_validator(value, default):
        return float(value) if value else default

    @staticmethod
    def _released_coef_validator(value, default):
        return float(value) if value else default


class CalculatorView(BaseView, CalculatorValidatorMixin):

    template_popup = {}
    data_popup = {}
    context_processors = []

    request_params_slots = {
        'spec': [None, None],
        'year': [None, None],
        'labor_coef': [None, None],
        'released_coef': [None, None],
        'delta_industry': [None, None]
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
            'data': None
        }
        super(CalculatorView, self).__init__(*args, **kwargs)

    def _render_popup_response(self, data=None):
        self.data_popup = data or {}
        return self._render()

    def _calculate(self):
        calculator = VacanciesCalculatorBL()
        spec = self.params_storage['spec']
        year = self.params_storage['year']
        params = dict(labor_coef=self.params_storage['labor_coef'],
                      released_coef=self.params_storage['released_coef'],
                      delta_industry=self.params_storage['delta_industry'])
        return calculator.calculate(spec=spec, year=year, **params)

    def post(self, *args, **kwargs):
        data = self._calculate()
        return self._render_popup_response({'calculate': data})
