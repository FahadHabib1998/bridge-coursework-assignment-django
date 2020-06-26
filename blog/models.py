from django.db import models

CV_TYPES = (
    ("1", "Work Experience"),
    ("2", "Education"),
    ("3", "Projects"),
    ("4", "Certification"),
)


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content =  models.TextField()
    addDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class CVElem(models.Model):
    type = models.CharField(
        max_length = 20,
        choices = CV_TYPES,
        default = '1'
        )
    name = models.CharField(max_length=100)
    emplyInti = models.CharField(max_length=100, blank = True, null=True)
    fromDate = models.DateField(blank=True, null=True)
    toDate = models.CharField(max_length= 50, blank=True)
    description =  models.TextField(null=True)

    def __str__(self):
        return self.type + ": " + self.name
