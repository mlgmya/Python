from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    
def movie(request):
    return render(request, 'movie.html')
    
def weather(request):
    return render(request, 'weather.html')

def phones(request):
    return render(request, 'phones.html')
