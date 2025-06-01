from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')
def about(request):
    """
    Render the about page.
    """
    return render(request, 'about.html')

