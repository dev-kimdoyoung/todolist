from django.shortcuts import render
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
