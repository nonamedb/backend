# coding: utf-8


import json
from django.http import JsonResponse
from django.conf import settings
from leon_base.base.views import BaseView
from layer_business.calculator import VacanciesCalculatorBL


PREDICTION_YEAR = 2019 + 4


class PredictionValidatorMixin:

    @staticmethod
    def _data_validator(value, default):
        return value if value else default


class PredictionView(BaseView, PredictionValidatorMixin):

    template_popup = {}
    data_popup = {}
    context_processors = []

    request_params_slots = {
        'data': [None, {}]
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
            'data': None
        }
        super(PredictionView, self).__init__(*args, **kwargs)

    def _render_popup_response(self, data=None):
        self.data_popup = data or {}
        return self._render()

    @staticmethod
    def _validate(data):
        assert isinstance(data, dict)
        for k, v in data.items():
            assert k in settings.SPECIALIZATIONS
            assert int(k)

    def _calculate(self, spec, year):
        calculator = VacanciesCalculatorBL()
        labor_coef = settings.LABOR_COEF
        released_coef = settings.RELEASED_COEF
        delta_industry = settings.DELTA_INDUSTRY
        params = dict(labor_coef=labor_coef,
                      released_coef=released_coef,
                      delta_industry=delta_industry)
        return calculator.calculate(spec=spec, year=year, **params)

    def get(self, *args, **kwargs):
        res = []
        for spec_abbr, spec_label in settings.SPECIALIZATIONS.items():
            prediction = self._calculate(spec_abbr, PREDICTION_YEAR)
            res.append({
                'label': spec_label,
                'abbr': spec_abbr,
                'current': 5,
                'prediction': prediction,
                'students': 5
            })
        return self._render_popup_response({'data': res})

    def post(self, *args, **kwargs):
        post_data = self.params_storage['data']
        res = []
        for spec_abbr, spec_label in settings.SPECIALIZATIONS:
            prediction = self._calculate(spec_abbr, PREDICTION_YEAR)
            res.append({
                'label': spec_label,
                'abbr': spec_abbr,
                'current': 5,
                'prediction': prediction,
                'students': 5
            })
        return self._render_popup_response({'data': res})
