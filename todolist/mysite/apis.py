import datetime

# Todolist DB import
from .models import TodoList
# Django에 내장된 models
from django.contrib.auth.models import User
# rest_framework
from rest_framework import serializers, viewsets


# User 정보의 표현을 정의
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','is_staff']


# TodoList 정보의 표현을 정의
class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ['url', 'user', 'contents', 'pub_date', 'exp_date', 'is_checked']


# User CRUD 정의
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TodoList CRUD 정의
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer