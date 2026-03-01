from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'collection/home.html')

def about_view(request):
    return render(request, 'collection/about.html')