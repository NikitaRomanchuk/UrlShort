from .models import ShortUrl
from django.forms import TextInput, ModelForm


class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['original_url']
        widgets = {'original_url': TextInput(attrs={
            'class': 'form-control',
            'name': 'original_url',
            'id': 'original_url',
            'placeHolder': 'Input your url',
        })
        }

