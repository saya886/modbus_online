from django.urls import path
from .views import *
from .api import *

app_name = 'modbus_view'

urlpatterns = [
path('index/',index_view.as_view(),name='index'),
]