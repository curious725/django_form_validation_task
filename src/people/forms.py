from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Contact


def validate_name(name):
    if len(name) < 2:
        raise ValidationError('Ensure this value has at least 2 characters')
    if len(name) > 50:
        raise ValidationError('Ensure this value has at most 50 characters')


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
        validators=[validate_name],
        help_text="*required Name field should have at least 2 and at most 50 characters."
    )
    phone = forms.CharField(
        validators=[validate_phone],
        required=False,
        widget=forms.TextInput(attrs={'pattern': '[0-9]{5-13}'}),
        help_text="*required Phone field should have from 5 till 13 digits"
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']
