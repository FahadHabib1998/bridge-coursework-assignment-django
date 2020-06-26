from django import forms

from .models import CVElem

class CvForm(forms.ModelForm):

    class Meta:
        model = CVElem
        fields = ('type', 'name', 'emplyInti','fromDate','toDate','description',)
