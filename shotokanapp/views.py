from django.http import request
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import StudentForm, kyu_creation_form
from .models import Student_info


def student_creation(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'student_creation.html', {'form': form})


def student_list(request):
    students = Student_info.objects.all()
    return render(request, 'student_get.html', {'students': students})


# def student_creation_get(request):
#     if request.method == 'GET':
#         # Retrieve the data from the database
#         students = student_creation.objects.all()
#         return render(request, 'student_get.html', {'students': students})
#     else:
#         form = StudentForm()
#         return render(request, 'student_get.html', {'form': form})


def kyu_creation_view(request):
    if request.method == 'POST':
        form = kyu_creation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = kyu_creation_form()
    return render(request, 'kyu_creation.html', {'form': form})


class firstpage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
        }
        return render(request, 'index.html', context)


def success_page(request):
    return render(request, 'success_page.html')


def edit_record(request, Student_ID):
    editrecord = Student_info.objects.get(Student_ID=Student_ID)
    return render(request, 'edit_record.html', {'student': editrecord})