from apps.models import Car
from django import forms


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'model',
            'brand',
            'image',
            'year',
            'overview',
            'price',
            'color',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'content': forms.Textarea(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }