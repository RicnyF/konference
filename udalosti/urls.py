from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.SessionListView.as_view(), name='session_list'),
    path('detail/<int:pk>', views.SessionDetailView.as_view(), name='session_detail'),
]
