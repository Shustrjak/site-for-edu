from django.urls import path, include
from .tasks import contact_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact'),
]