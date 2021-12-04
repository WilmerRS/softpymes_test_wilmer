# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)


@api.route('/examples', methods=['GET'])
def get_all_examples():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    query = request.args.get('query')

    response = Controller.get_all_examples(page=page, per_page=per_page, query=query)
    return jsonify(data=response)


@api.route('/examples/<id>', methods=['PUT'])
def create_example(id):
    response = Controller.create_example(id, request)
    return jsonify(data=response)
