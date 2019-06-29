import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList

def index(request):
    # contents_list에 TodoList의 전체 내용을 객체로 저장
    contents_list = TodoList.objects.all()

    # context 자료형에 contents_list 객체를 저장
    context = {
        'contents_list':contents_list
    }
    # index.html 파일에 context를 rendering
    return render(request,'mysite/index.html', context)

def list_add(request):
    # request.POST에 html에서 http 메소드 중 POST로 <form> 안의 데이터를 전달할 때
    # POST 안에서 dictionary 객체로 존재한다.
    content_name = request.POST['add_content']
    pub_date = datetime.datetime.now()
    exp_date = request.POST['exp_date']

    # 할 일 : return으로 Django에서 lib로 제공하는 message 리턴
    model_instance = TodoList.objects.create(contents=content_name,pub_date=pub_date,
                                          exp_date=exp_date)
    return HttpResponse(exp_date)

# 장고 DB 활용 관련
# https://brownbears.tistory.com/63
# https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/