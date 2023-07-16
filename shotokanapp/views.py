from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import StudentForm


class firstpage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
        }
        return render(request, 'index.html', context)


class CreateStudent(TemplateView):
    template_name = 'create_student.html' 

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})





