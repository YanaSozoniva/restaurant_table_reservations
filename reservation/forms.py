from django import forms
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField

from users.forms import StyleFormMixin


class ContactForm(StyleFormMixin, forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator()])
    phone = PhoneNumberField(required=False)
    message = forms.CharField(widget=forms.Textarea)
