from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('minis/', views.miniatures_list_view, name='miniatures-list'),
    path('minis/<int:id>/', views.miniature_detail_view, name='miniature-detail'),
]