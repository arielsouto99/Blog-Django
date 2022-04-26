from django import forms
# Models
from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):

    class Meta:
        model = Suscribers
        fields = [
            'email',
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'Email...',
                }
            ),
        }
    
# Formulario para contacto que funciona en todos los templates
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')