from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(max_length=100)   #描述功能 最大限制字数100
    #创建后在admin中注册


