from django.urls import path, include
from .views import index_view
app_name = 'mynews'

urlpatterns = [
    path('', index_view, name='index'),
]
