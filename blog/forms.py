from django import forms

from .models import Publicar

class PostearForm(forms.ModelForm):

    class Meta:
        model = Publicar
        fields = ('titulo','texto',)
