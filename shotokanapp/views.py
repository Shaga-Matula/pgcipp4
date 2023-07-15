from django.shortcuts import render
from django.views import View
from .forms import StudentLvlForm
from django.shortcuts import redirect


class firstpage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
        }
        return render(request, 'index.html', context)

from .forms import StudentLvlForm

def create_student_lvl(request):
    if request.method == 'POST':
        form = StudentLvlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = StudentLvlForm()
    return render(request, 'create_student_lvl.html', {'form': form})