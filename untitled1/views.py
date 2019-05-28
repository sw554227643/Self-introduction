from django.shortcuts import render
from gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects  #将变量传递过来的这个变量，将这个描述
    return render(request,'home.html',{'gallerys':gallerys}) #用字典传递到html中