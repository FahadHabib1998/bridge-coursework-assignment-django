from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('blog/',views.blogpage, name='blogpage'),
    path('blog/<int:pk>/',views.postpage, name='postpage'),
    path('cv/', views.cvmenu, name = 'cvmenu'),
    path('cv/new/', views.addnew, name='addnew'),
    path('post/edit/<int:pk>/', views.editcvelem, name='editcvelem'),
    path('cv/work_experience/', views.cvwork, name = 'cvwork'),
    path('cv/education/', views.cvedu, name = 'cvedu'),
    path('cv/project/', views.cvproj, name = 'cvproj'),
    path('cv/remove/<int:pk>', views.deleteelem, name='deleteelem'),
    path('accounts/login/', views.gotoadmin, name = 'gotoadmin' )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
