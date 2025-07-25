from rest_framework.pagination import PageNumberPagination

class MessageResultSetPagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page_size"
    max_page_size = 20