# coding: utf-8


import json
import random
from django.http import JsonResponse
from django.conf import settings
from leon_base.base.views import BaseView
from layer_business.predictor import PredictorBL


PREDICTION_YEAR = 2019 + 4


class PredictionValidatorMixin:

    @staticmethod
    def _data_validator(value, default):
        return json.loads(value) if value else default


class PredictionView(BaseView, PredictionValidatorMixin):

    template_popup = {}
    data_popup = {}
    context_processors = []

    request_params_slots = {
        'data': [None, []]
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

    def _calculate(self, spec, year, students_data=None):
        calculator = PredictorBL()
        return calculator.calculate(spec=spec, year=year, students_data=students_data)

    def _get_vacancies(self, spec, year):
        calculator = PredictorBL()
        return calculator.get_vacancies(spec, year)

    def _get_students(self, spec, year):
        calculator = PredictorBL()
        return calculator.get_students(spec, year)

    def _get_new_students(self, spec, data):
        for item in data:
            if spec in item:
                return item[spec]

    def get(self, *args, **kwargs):
        res = []
        for spec_abbr, spec_label in settings.SPECIALIZATIONS.items():
            prediction = self._calculate(spec_abbr, PREDICTION_YEAR)
            current = self._get_vacancies(spec_abbr, PREDICTION_YEAR)
            students = self._get_students(spec_abbr, PREDICTION_YEAR)
            res.append({
                'label': spec_label,
                'abbr': spec_abbr,
                'current': current,
                'prediction': prediction,
                'students': students
            })
        return self._render_popup_response({'data': res})

    def post(self, *args, **kwargs):
        post_data = self.params_storage['data']
        res = []
        for spec_abbr, spec_label in settings.SPECIALIZATIONS.items():
            students = self._get_new_students(spec_abbr, post_data)
            prediction = self._calculate(spec_abbr, PREDICTION_YEAR,
                                         {'year': PREDICTION_YEAR, 'received': students})
            current = self._get_vacancies(spec_abbr, PREDICTION_YEAR)
            res.append({
                'label': spec_label,
                'abbr': spec_abbr,
                'current': current,
                'prediction': prediction,
                'students': students
            })
        return self._render_popup_response({'data': res})
