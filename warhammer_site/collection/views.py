from django.shortcuts import render
from .models import Miniature

# Create your views here.
def home_view(request):
    return render(request, 'collection/home.html')

def miniatures_list_view(request):
    miniatures = Miniature.objects.all().order_by('-created_at')
    return render(
        request,
        'collection/miniatures_list.html',
        {'miniatures': miniatures}
    )

def about_view(request):
    return render(request, 'collection/about.html')