from django.shortcuts import render, get_object_or_404
from .models import BlogPost, CVElem
from .forms import CvForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.storage import staticfiles_storage
import mimetypes
from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return render(request,'blog/mainpage.html',{})

def blogpage(request):
    posts = BlogPost.objects
    return render(request,'blog/blogpage.html',{'posts': posts})

def postpage(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog/postpage.html', {'post': post})

def cvmenu(request):
    return render(request,'blog/cvpage.html',{})

@login_required
def addnew(request):
    if request.method == "POST":
        form = CvForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
        if form.data['type'] == "1":
            return redirect('cvwork')
        elif form.data['type'] == "2":
            return redirect('cvedu')
        else:
            return redirect('cvproj')
    else:
        form = CvForm()
    return render(request, 'blog/addcvelem.html', {'form': form})
@login_required
def editcvelem(request, pk):
    post = get_object_or_404(CVElem, pk=pk)
    if request.method == "POST":
        form = CvForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            if form.data['type'] == "1":
                return redirect('cvwork')
            elif form.data['type'] == "2":
                return redirect('cvedu')
            else:
                return redirect('cvproj')
    else:
        form = CvForm(instance=post)
    return render(request, 'blog/addcvelem.html', {'form': form})

def cvwork(request):
    datas = CVElem.objects
    return render(request,'blog/cvwork.html',{'datas': datas})

def cvedu(request):
    datas = CVElem.objects
    return render(request,'blog/cvedu.html',{'datas': datas})

def cvproj(request):
    datas = CVElem.objects
    return render(request,'blog/cvproj.html',{'datas': datas})

@login_required
def deleteelem(request, pk):

    elem = get_object_or_404(CVElem, pk=pk)
    type = 0

    if elem.type == "1":
        type = 1
    elif elem.type == "2":
        type = 2
    elif elem.type == "3":
        type = 3
    print(type)
    elem.delete()

    if type == 1:
        return redirect('cvwork')
    elif type == 2:
        return redirect('cvedu')
    elif type == 3:
        return redirect('cvproj')

def gotoadmin(request):
    return render(request,'blog/gotoadmin.html',{})

'''def downloadcv(request):

    fl_path = staticfiles_storage.path('CVPDF.pdf')
    filename = 'CVPDF.pdf'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response'''
