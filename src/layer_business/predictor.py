# coding: utf-8


import os
import json

from config.settings import STATISTICS_ROOT, ROOT_PATH


class PredictorBL:

    def _calculate(self, vacancies_start_data, year, **params):
        if vacancies_start_data['year'] >= year:
            return vacancies_start_data['vacancies']
        return self._calculate(vacancies_start_data, year-1, **params)

    def _received_students(self, students_start_data, year, **params):
        if students_start_data['year'] >= year:
            return students_start_data['received']
        return self._received_students(students_start_data, year-1, **params)

    def _load_coefs(self, spec):
        return self._load_file(os.path.join(STATISTICS_ROOT, '{}_{}.json'.format('coef', spec)))

    @staticmethod
    def _load_file(filename):
        with open(os.path.join(ROOT_PATH, filename), 'r') as f:
            return json.loads(f.read())

    def get_vacancies(self, spec, year):
        vacancies_start_data = self.load_start_data('vacancies', spec)
        return vacancies_start_data['vacancies']

    def get_students(self, spec, year):
        students_start_data = self.load_start_data('students', spec)
        return students_start_data['received']

    def calculate(self, spec, year, students_data=None):
        coefs = self._load_coefs(spec)

        released_coef = coefs['released_coef']
        labor_coef = coefs['labor_coef']
        delta_industry = coefs['delta_industry']

        vacancies_start_data = self.load_start_data('vacancies', spec)
        students_start_data = students_data or self.load_start_data('students', spec)
        res = self._calculate(vacancies_start_data, year - 1) * (1 + delta_industry) - \
            self._received_students(students_start_data, year - 4) * released_coef * labor_coef
        return int(res) if res else 0

    def load_params(self):
        pass

    def load_start_data(self, dataset_type, spec):
        return self._load_file(os.path.join(STATISTICS_ROOT, '{}_{}.json'.format(dataset_type, spec)))
