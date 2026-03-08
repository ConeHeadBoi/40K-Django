from django import forms
from .models import Miniature, Faction

class MiniatureForm(forms.ModelForm):
    class Meta:
        model = Miniature
        fields = [
            'name',
            'faction',
            'points',
            'description',
            'painting_stage',
            'image',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })