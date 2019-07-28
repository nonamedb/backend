# coding: utf-8


import json
from django.http import JsonResponse
from leon_base.base.views import BaseView
from layer_business.calculator import VacanciesCalculatorBL


class StatisticsValidatorMixin:

    @staticmethod
    def _spec_validator(value, default):
        return value if value else default

    @staticmethod
    def _year_validator(value, default):
        return value if value else default

    @staticmethod
    def _dataset_validator(value, default):
        return value if value else default


class StatisticsView(BaseView, StatisticsValidatorMixin):

    template_popup = {}
    data_popup = {}
    context_processors = []

    request_params_slots = {
        'spec': [None, None],
        'year': [None, None],
        'dataset': [None, None],
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
            'data': None
        }
        super(StatisticsView, self).__init__(*args, **kwargs)

    def _render_popup_response(self, data=None):
        self.data_popup = data or {}
        return self._render()

    def get(self):
        return self._render_popup_response()
