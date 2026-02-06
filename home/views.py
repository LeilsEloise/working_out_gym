from django.shortcuts import render

# Create your views here.
def home(request):
    """View returns the Home page"""
    return render(request, 'home/index.html')