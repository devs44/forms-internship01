from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['complete','todotext']

        widgets={
        'todotext':forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'todotext'
        })
    }
