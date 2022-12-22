from rest_framework.pagination import PageNumberPagination

menu = [{'title': "О сайте", 'url_name': 'about'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

class MedicAPIPagination(PageNumberPagination):
     page_size = 3
     page_size_query_param = 'page_size'
     max_page_size = 5
