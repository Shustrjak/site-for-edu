from django.urls import path
from .t_views import index_view

app_name = 'teacher'

urlpatterns = [
    path('', index_view, name='index'),
]