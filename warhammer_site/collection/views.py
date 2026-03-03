from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import MiniatureForm
from .models import Miniature

# Create your views here.
# View for the home page of the collection
def home_view(request):
    return render(request, 'collection/home.html')

# View for the about page of the collection
def about_view(request):
    return render(request, 'collection/about.html')

# View for displaying the details of a specific miniature
def miniatures_list_view(request):
    miniatures = Miniature.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    faction = request.GET.get('faction')

    if query:
        miniatures = miniatures.filter(name__icontains=query)

    if faction:
        miniatures = miniatures.filter(faction__iexact=faction)

    factions = Miniature.objects.values_list('faction', flat=True).distinct()

    return render(
        request,
        'collection/miniatures_list.html',
        {
            'miniatures': miniatures,
            'factions': factions,
        }
    )

# View for displaying the details of a specific miniature
def miniature_detail_view(request, id):
    miniature = get_object_or_404(Miniature, id=id)
    return render(
        request,
        'collection/miniature_detail.html',
        {'miniature': miniature}
    )

# View for creating a new miniature
def miniature_create_view(request):
    if request.method == 'POST':
        form = MiniatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('miniatures-list')
    else:
        form = MiniatureForm()

    return render(
        request,
        'collection/miniature_form.html',
        {'form': form}
    )

# View for updating an existing miniature
def miniature_update_view(request, id):
    miniature = get_object_or_404(Miniature, id=id)

    if request.method == 'POST':
        form = MiniatureForm(request.POST, request.FILES, instance=miniature)
        if form.is_valid():
            form.save()
            return redirect('miniatures-list')
    else:
        form = MiniatureForm(instance=miniature)

    return render(
        request,
        'collection/miniature_form.html',
        {'form': form}
    )

# View for deleting a miniature
def miniature_delete_view(request, id):
    miniature = get_object_or_404(Miniature, id=id)

    if request.method == 'POST':
        miniature.delete()
        return redirect('miniatures-list')

    return render(
        request,
        'collection/miniature_confirm_delete.html',
        {'miniature': miniature}
    )