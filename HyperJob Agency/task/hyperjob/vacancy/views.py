from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View

from .models import Vacancy


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy.html', context={'vacancies': vacancies})


class VacancyCreateView(View):
    def get(self, request):
        return render(request, 'vacancy_create.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.filter(username=request.user)
            try:
                if user.is_staff:
                    resume = Vacancy(description=request.POST.get('description'), author=request.user)
                    resume.save()
                    return redirect("/home/")
                else:
                    return HttpResponseForbidden()
            except:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
