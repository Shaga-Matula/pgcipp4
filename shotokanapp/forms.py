from django import forms
from .models import Student_Lvl

class StudentLvlForm(forms.ModelForm):
    class Meta:
        model = Student_Lvl
        fields = ['kyu_level', 'belt_color', 'kata_name',  'kata_image', 'syllabus_image']

