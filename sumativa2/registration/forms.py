from .models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'photo']
        widgets = {
            'username': forms.TextInput({'class' : 'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class' : 'form-control'})
        }