from rest_framework.pagination import CursorPagination

class WatchListCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'title'
    cursor_query_param = 'data'