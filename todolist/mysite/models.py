import datetime

from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    # on_delete = models.CASCADE를 통해 User의 PK가 삭제되면
    # 이에 대응하는 FK 또한 삭제된다.
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    is_checked = models.BooleanField()
    contents = models.CharField(max_length=100)
    pub_date = models.DateTimeField('published_date', default=datetime.datetime.now())
    exp_date = models.DateTimeField('expire_date', null=True, blank=True)
