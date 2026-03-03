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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['painted'].widget.attrs.update({
            'class': 'form-check-input'
        })