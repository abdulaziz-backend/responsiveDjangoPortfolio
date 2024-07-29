from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'placeholder': 'Your Email',
                'required': True
                }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'placeholder': 'Your Message',
                'required': True
            }),
        }