from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_add/', views.list_add, name='list_add'),
]
