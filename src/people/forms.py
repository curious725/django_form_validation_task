from django.core.exceptions import ValidationError
from django import forms
from .models import Contact


def validate_name(name):
    if len(name) < 2:
        raise ValidationError('Ensure this value has at least 2 characters')


def validate_phone(phone):
    try:
        int(phone)
    except ValueError:
        raise ValidationError('Phone number can include only digits.')
    if len(phone) < 5 or len(phone) > 13:
        raise ValidationError(
            'Ensure this value has at least 5 digits and less than 14 digits'
        )


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validate_name]
    )
    phone = forms.CharField(
        validators=[validate_phone],
        widget=forms.TextInput(
            attrs={'pattern': '[0-9]{5-13}', 'title': 'Enter digits only'}
        )
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']
