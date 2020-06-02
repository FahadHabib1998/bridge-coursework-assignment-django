from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost
from .models import CVElem

admin.site.register(BlogPost)
admin.site.register(CVElem)
