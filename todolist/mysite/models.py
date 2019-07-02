from django.db import models

class TodoList(models.Model):
    is_checked = models.BooleanField()
    contents = models.CharField(max_length=100)
    pub_date = models.DateTimeField('published_date')
    exp_date = models.DateTimeField('expire_date', null=True)
