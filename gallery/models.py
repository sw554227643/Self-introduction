from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='在这里写作品的简介',max_length=100)   #描述功能 最大限制字数100
    #创建后在admin中注册
    image = models.ImageField(default = 'default.png',upload_to='images/') #默认图片默认路径
    title = models.CharField(default = '作品标题',max_length=50)

    def __str__(self):
        return self.title

