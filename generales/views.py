from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return render(request, "home.html")


def home(request):
    return render(request, 'index.html')


