from django import forms
from .models import Student_info

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_info
        fields = [
            'first_name',
            'last_name',
            'Date_of_birth',
            'Email',
            'Address_1',
            'Address_2',
            'Student_Grade',
            ]

