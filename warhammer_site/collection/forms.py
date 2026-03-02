from django import forms
from .models import Miniature

class MiniatureForm(forms.ModelForm):
    class Meta:
        model = Miniature
        fields = [
            'name',
            'faction',
            'points',
            'description',
            'painted',
            'image',
        ]