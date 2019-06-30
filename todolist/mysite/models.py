from django.db import models

class TodoList(models.Model):
    is_Checked = models.IntegerField(default=0)
    contents = models.CharField(max_length=100)
    pub_date = models.DateTimeField('published_date')
    exp_date = models.DateTimeField('expire_date')
