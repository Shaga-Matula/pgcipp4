from django.shortcuts import render
from django.views import generic, View

# Create your views here.


class firstpage(View):

    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,

        }
        return render(request, 'index.html', context)


class form_page(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'form_page.html',)
