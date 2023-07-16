from django.views import View
from django.shortcuts import render
from django.http import request
from .forms import StudentForm

def student_creation(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'student_creation.html', {'form': form})

class firstpage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
        }
        return render(request, 'index.html', context)

def success_page(request):
    return render(request, 'success_page.html')
