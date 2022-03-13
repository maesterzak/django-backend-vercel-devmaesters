from rest_framework.response import Response
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):

    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'ps'
    limit_query_param='l'
    pax_limit=9

    def get_paginated_response(self, data):
        response = Response(data)
        return response
