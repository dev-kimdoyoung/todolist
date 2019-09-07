from django.urls import path, include
from . import views
from rest_framework import routers
# apis 앞에 .을 붙여서 나랑 같은 디렉토리에 존재한다는 것을 명시
from .apis import UserViewSet, TodoListViewSet


# routers : 장고에서 사용하는 url
# DefaultRouter() : URL conf
# REST API 경로 설정
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'TodoList', TodoListViewSet)


# urlpatterns : django 에서 url conf(configuration) 역할
urlpatterns = [
    path('', views.index, name='index'),
    path('list_add/', views.list_add, name='list_add'),
    path('list_delete/', views.list_delete, name='list_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
