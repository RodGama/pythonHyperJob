from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden

from .models import Resume


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume.html', context={'resumes': resumes})


class ResumeCreateView(View):
    def get(self, request):
        return render(request, 'resume_create.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            resume = Resume(description=request.POST.get('description'), author=request.user)
            resume.save()
            return redirect("/home/")
        else:
            return HttpResponseForbidden()
