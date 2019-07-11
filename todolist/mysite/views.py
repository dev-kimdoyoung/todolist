import datetime

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoList
from django.contrib import messages, auth
from django.contrib.auth.models import User

def index(request):
    user = request.user
    if user.id is None:
        return redirect("login/")

    if request.method == "POST":
        if request.POST["content_id"] is None:
            content = TodoList.objects.filter(user=user)
            content.exp_date = datetime.datetime.now()
            content.is_checked = True
        else:
            content = TodoList.objects.get(pk=request.POST["content_id"])
            content.exp_date = datetime.datetime.now()
            content.is_checked = True
            content.save()

    contents_list = TodoList.objects.filter(user=user)
    # context 자료형에 contents_list 객체를 저장
    context = {
            'contents_list': contents_list
    }
    # index.html 파일에 context를 rendering
    return render(request, 'mysite/index.html', context)
    # get : DB에 직접 접근하여 해당 결과물을 객체로 가져온 형태
    # filter : DB에 결과물 조건만 매핑시켜놓고 아직 접근하지 않은 형태
            # Sql 코드를 짤 준비만 해놓고 아직 컴파일은 하지 않은 상태
    # filter는 list를 return하고, get은 한 개의 객체를 return한다.
    # contents_list에 TodoList의 전체 내용을 저장

def list_add(request):
    # request.POST에 html에서 http 메소드 중 POST로 <form> 안의 데이터를 전달할 때
    # POST 안에서 dictionary 객체로 존재한다.

    content_name = request.POST['add_content']
    pub_date = datetime.datetime.now()
    exp_date = request.POST['exp_date']
    user = request.user

    if content_name == "":
        messages.add_message(request, messages.INFO, '추가할 내용을 입력해주세요!')
        return HttpResponseRedirect("/")

    if exp_date:
        TodoList.objects.create(user=user, is_checked=False, contents=content_name, pub_date=pub_date, exp_date=exp_date)
    else:
        TodoList.objects.create(user=user, is_checked=False, contents=content_name, pub_date=pub_date, exp_date=None)
    messages.add_message(request, messages.INFO, '일정이 추가되었습니다.')
    return HttpResponseRedirect("/")


def list_delete(request):
    if request.method == 'POST':
        if request.POST['delete_content'] == "":
            messages.add_message(request, messages.INFO, '삭제할 내용을 입력해주세요!')
            return HttpResponseRedirect("/")
        pk = TodoList.objects.filter(contents=request.POST['delete_content'])
        pk.delete()
        messages.add_message(request, messages.INFO, '데이터가 삭제되었습니다.')
        return redirect('/')
    else:
        messages.add_message(request, messages.INFO, '데이터가 잘못 입력되었습니다.')
        return redirect('/')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        pw = request.POST["pw"]
        if username == "" or pw == "":
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 입력해주세요!')
        else:
            user = authenticate(username=username, password=pw)

            if user is not None:
                messages.add_message(request, messages.INFO, '이미 존재하는 아이디입니다.')
                return render(request, 'mysite/register.html')
            else:
                user = User.objects.create_user(username=username, email=None, password=pw)
                user.save()
                messages.add_message(request, messages.INFO, '회원가입 완료!!')
                return render(request, 'mysite/login.html')

    return render(request, 'mysite/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pw = request.POST["pw"]

        if username == "" or pw == "":
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 입력해주세요!')
        # user 데이터가 존재한다면
        else:
            user = authenticate(username=username, password=pw)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
    #            return render(request, 'mysite/index.html/')
            else:
                messages.add_message(request, messages.INFO, 'ID와 비밀번호가 일치하지 않습니다.')

    return render(request, 'mysite/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # user 객체를 POST로 받아와야 한다.
        return render(request, 'mysite/login.html/')

# 장고 DB 활용 관련
# https://brownbears.tistory.com/63
# https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/

# ctrl + / : 주석처리
