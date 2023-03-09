from django.urls import path
from .views import *

urlpatterns = [
    path('', analisis_sentimientos , name='analisis_sentimientos'),
]