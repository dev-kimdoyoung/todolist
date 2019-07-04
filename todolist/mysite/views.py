import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, User
from django.contrib import messages, auth
from django.contrib.auth.models import User


def index(request):

    if request.method == "POST":
        content_id = request.POST["content_id"]
        content = TodoList.objects.get(pk=content_id)
        content.exp_date = datetime.datetime.now()
        content.is_checked = True
        content.save()

    # get : DB에 직접 접근하여 해당 결과물을 객체로 가져온 형태
    # filter : DB에 결과물 조건만 매핑시켜놓고 아직 접근하지 않은 형태
            # Sql 코드를 짤 준비만 해놓고 아직 컴파일은 하지 않은 상태

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

    content_name = request.POST['add_content']
    pub_date = datetime.datetime.now()
    exp_date = request.POST['exp_date']

    if exp_date:
        TodoList.objects.create(is_checked=False, contents=content_name, pub_date=pub_date, exp_date=exp_date)
    else:
        TodoList.objects.create(is_checked=False, contents=content_name, pub_date=pub_date, exp_date=None)
    messages.add_message(request, messages.INFO, '일정이 추가되었습니다.')
    return HttpResponseRedirect('/')


def list_delete(request):
    if request.method == 'POST':
        pk = TodoList.objects.get(pk=request.POST['delete_content'])
        pk.delete()
        messages.add_message(request, messages.INFO, '데이터가 삭제되었습니다.')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.INFO, '데이터가 잘못 입력되었습니다.')
        return HttpResponseRedirect('/')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, "/")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        pw = request.POST["pw"]
        user = auth.authenticate(request, username=username, pw=pw)
        if user is not None:
            messages.add_message(request, messages.INFO, '이미 존재하는 username입니다.')
        else:
            User.objects.create(username=username, passwd=pw)
            messages.add_message(request, messages.INFO, '회원가입이 완료되었습니다.')
            return HttpResponse(username)

    return render(request, 'mysite/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pw = request.POST["pw"]

        # username과 passwd가 맞으면 is_login_session을 True로 DB에 저장하는 작업
        # 관리자 계정으로 들어가서 username과 passwd가 일치하는 데이터가 있는지 확인
        user = auth.authenticate(request, username=username, pw=pw)

        # user 데이터가 존재하다면
        if user is not None:
            # user로 로그인 요청
            auth.login(request, user)
            messages.add_message(request, messages.INFO, '로그인 완료!')
        else:
            messages.add_message(request, messages.INFO, 'ID와 비밀번호가 일치하지 않습니다.')

    return render(request, 'mysite/login.html')


# 장고 DB 활용 관련
# https://brownbears.tistory.com/63
# https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/

# ctrl + / : 주석처리