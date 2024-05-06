# V souboru urls.py vaší aplikace
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
]