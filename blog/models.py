from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content =  models.TextField()
    addDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class CVElem(models.Model):
    title = models.CharField(max_length=200)
    content =  models.TextField()
    addDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
