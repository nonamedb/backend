# coding: utf-8


import os
import json
from django.forms.models import model_to_dict

from config.settings import STATISTICS_ROOT


class VacanciesCalculatorBL:

    def _calculate(self, vacancies_start_data, year, **params):
        if vacancies_start_data['year'] == year:
            return vacancies_start_data['vacancies']
        return self._calculate(vacancies_start_data, year-1, **params)

    def _labor_students(self, students_start_data, year, **params):
        released_coef = params['released_coef']
        labor_coef = params['labor_coef']
        if students_start_data['year'] >= year:
            return students_start_data['labor'] * released_coef * released_coef * labor_coef
        return self._labor_students(students_start_data, year-1, **params)

    @staticmethod
    def _load_file(filename):
        with open(filename, 'r'):
            return json.loads(filename)

    def calculate(self, spec, year, **params):
        vacancies_start_data = self.load_start_data('vacancies', spec)
        students_start_data = self.load_start_data('students', spec)
        delta_industry = params['delta_industry']
        return self._calculate(vacancies_start_data, year - 1, **params) * (1 + delta_industry) - \
            self._labor_students(students_start_data, year - 4, **params)

    def load_params(self):
        pass

    def load_start_data(self, dataset_type, spec):
        return self._load_file(os.path.join(STATISTICS_ROOT, '{}_{}.json'.format(dataset_type, spec)))
