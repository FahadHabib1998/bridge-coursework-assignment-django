from django.shortcuts import render
from .models import BlogPost, CVElem

# Create your views here.
def mainpage(request):
    return render(request,'blog/mainpage.html',{})

def blogpage(request):
    posts = BlogPost.objects
    return render(request,'blog/blogpage.html',{'posts': posts})

def cvpage(request):
    data = CVElem.objects
    return render(request,'blog/cvpage.html',{'data': data})
