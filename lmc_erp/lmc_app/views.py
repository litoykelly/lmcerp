from django.shortcuts import render
from lmc_app.models import Employe,Grade
# Create your views here.


def accueil(request):
    return render(request, 'lmc_app/accueil.html')


def grade(request):
    grades = Grade.objects.all()
    return render(request, 'lmc_app/grade.html',{'grades': grades})

def fonction(request):
    return render(request, 'lmc_app/fonction.html')

def employe(request):
    employes = Employe.objects.all()
    return render(request, 'lmc_app/employe.html', {'employes' : employes})


def employe_detail(request, id):
    employe = Employe.objects.get(pk=id)
    return render(request, 'lmc_app/employe_detail.html', {'employe': employe})


