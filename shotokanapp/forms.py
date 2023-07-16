from django import forms
<<<<<<< HEAD
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
=======
from .models import Student_Lvl, Student_info


# class StudentLvlForm(forms.ModelForm):
#     class Meta:
#         model = Student_Lvl
#         fields = ['kyu_level', 'belt_color',
#                   'kata_name',  'kata_image', 'syllabus_image']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_info
        fields = ['first_name', 'last_name', 'Date_of_birth', 'Email', 'Address_1', 'Address_2', 'Student_Grade',]
>>>>>>> eb2f6c1777b1c543e023b76ec57259ad202f725f

# class StudentInfoForm(forms.ModelForm):
#     class Meta:
#         model = Student_info
#      