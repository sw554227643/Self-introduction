from django.contrib import admin
from .models import Gallery #从本级modles模块中导入Gallery 文件

# Register your models here.

admin.site.register(Gallery)    #注册modle
