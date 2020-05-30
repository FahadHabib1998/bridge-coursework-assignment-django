from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def mainpage(request):
    return render(request,'blog/mainpage.html',{})

def blogpage(request):
    posts = BlogPost.objects
    return render(request,'blog/blogpage.html',{'posts': posts})
