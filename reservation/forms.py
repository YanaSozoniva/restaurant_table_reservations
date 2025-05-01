from django import forms
from phonenumber_field.formfields import PhoneNumberField

from users.forms import StyleFormMixin


class ContactForm(StyleFormMixin, forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = PhoneNumberField(required=False)
    message = forms.CharField(widget=forms.Textarea)
