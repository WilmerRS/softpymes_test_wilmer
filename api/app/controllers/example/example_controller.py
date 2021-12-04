# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel
from app import db

# use cases
from app.use_cases.example.SearchExamples import SearchExamples
from app.use_cases.example.CreateExamples import CreateExamples


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_all_examples(page, per_page, query):
        try:
            page = int(page)
            per_page = int(per_page)
            _use_case = SearchExamples()
            result = _use_case.get(page, per_page, query)
            response = {
                'result': result,
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except ValueError as e:
            response = {
                'ok': False,
                'message': 'Page and per page should be integers.'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def create_example(id, request):
        try:
            body = request.get_json()
            to_create = {
                'id': id,
                'name': body['name'],
                'identification': body['identification'],
                'description': body['description'],
                'status': body['status']
            }
            _use_case = CreateExamples()
            result = _use_case.save(**to_create)
            response = {
                'result': result,
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
