from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """ Класс для постраничного вывода"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20



