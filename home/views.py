from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


def statistics(request):

    # Page from the theme 
    return render(request, 'pages/statistics.html')


def sustainability(request):

    # Page from the theme 
    return render(request, 'pages/sustainability.html')



def model_explanation(request):

    # Page from the theme 
    return render(request, 'pages/model_explanation.html')