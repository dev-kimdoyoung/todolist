import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList
from django.contrib import messages


def index(request):
    # contents_list에 TodoList의 전체 내용을 저장
    contents_list = TodoList.objects.all()

    # context 자료형에 contents_list 객체를 저장
    context = {
        'contents_list': contents_list
    }
    # index.html 파일에 context를 rendering
    return render(request, 'mysite/index.html', context)


def list_add(request):
    # request.POST에 html에서 http 메소드 중 POST로 <form> 안의 데이터를 전달할 때
    # POST 안에서 dictionary 객체로 존재한다.
    if request.POST.getlist("is_checked[]"):
        is_check = request.POST.getlist("is_checked")
        queryset = TodoList.objects.get(pk=is_check)
        queryset.exp_date = datetime.datetime.now()
        queryset.save()

    content_name = request.POST['add_content']
    pub_date = datetime.datetime.now()
    exp_date = request.POST['exp_date']

    # 할 일 : return으로 Django에서 lib로 제공하는 message 리턴
    TodoList.objects.create(contents=content_name, pub_date=pub_date,exp_date=exp_date)
    messages.success(request, '데이터가 저장되었습니다.')
    return HttpResponseRedirect('/')


def list_delete(request):
    if request.method == 'POST':
        pk = TodoList.objects.get(pk=request.POST['delete_content'])
        pk.delete()
        messages.success(request, '데이터가 삭제되었습니다.')
        return HttpResponseRedirect('/')
    else:
        messages.error(request, '데이터가 잘못 입력되었습니다..')
        return HttpResponseRedirect('/')
# 장고 DB 활용 관련
# https://brownbears.tistory.com/63
# https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/
# 할 일
# 1. Django 내장 message 기능을 통해 사용자에게 성공 여부 전달
# 2. html에서 checkbox 체크가 되면 자동으로 만료일 update 해주기