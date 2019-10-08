# 파일 명은 "Dockerfile"로 하는게 좋음. 만약 하지 않으면, 나중에 빌드할 때 따로 옵션을 주어야 하는 번거로움이 있음

# python 3.6을 불러옴
FROM python:3.6

# 작업할 디렉토리 경로 설정 (없으면 해당 디렉토리를 생성한다.)
WORKDIR /app

# todolist(host machine) 디렉토리를 /app(이미지 파일을 저장할 경로)에 복사한다.
COPY todolist /app
COPY requirements.txt /meta/requirements.txt

# pipenv lock -r : Pipfile.lock 파일에 써져있는 의존성 리스트를 읽어들임
# 리눅스에서 '>'는 "왼쪽 내용을 오른쪽 파일에 써라"라는 의미
# pipenv lock -r > requirements.txt : 해당 프로젝트의 의존성 목록을 requirements.txt에 저장
# -r : 해당 파일에서 의존성 리스트를 읽어들이겠다는 의미

# requirements.txt에 저장된 의존성 리스트에 따라 해당 개발환경에 패키지를 설치
# pipenv는 따로 설치해야 하기 때문에 이미지를 가볍게 하기 위해서 pip를 사용
RUN pip install -r /meta/requirements.txt

# 보통 ENV(환경변수 설정) 명령어는
# 프로토콜://USER:PASSWORD@HOST:PORT/NAME
# 3306이 MySQL의 표준 포트이고, Django의 경우 NAME은 프로젝트 이름으로 한다.
ENV DB_URL mysql://kimdoyoung:01022074992@db:3306/todolist

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0"]
