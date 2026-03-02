from django.shortcuts import render
from .models import Miniature
from django.shortcuts import get_object_or_404

# Create your views here.
# View for the home page of the collection
def home_view(request):
    return render(request, 'collection/home.html')

# View for displaying the details of a specific miniature
def miniatures_list_view(request):
    miniatures = Miniature.objects.all().order_by('-created_at')
    return render(
        request,
        'collection/miniatures_list.html',
        {'miniatures': miniatures}
    )

# View for displaying the details of a specific miniature
def miniature_detail_view(request, id):
    miniature = get_object_or_404(Miniature, id=id)
    return render(
        request,
        'collection/miniature_detail.html',
        {'miniature': miniature}
    )

# View for the about page of the collection
def about_view(request):
    return render(request, 'collection/about.html')