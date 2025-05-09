from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField

from reservation.models import Reservation, Table
from users.forms import StyleFormMixin


class ContactForm(StyleFormMixin, forms.Form):
    """Форма обратной связи"""

    name = forms.CharField(max_length=100, label="Имя")
    email = forms.EmailField(validators=[EmailValidator()], label="Почта")
    phone = PhoneNumberField(required=False, label="Телефон")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")


class ReservationForm(StyleFormMixin, forms.ModelForm):
    """Форма нового бронирования"""

    class Meta:
        model = Reservation
        exclude = ("customer",)

    def clean_date_reserved(self):
        """Валидация даты бронирования"""
        date_reserved = self.cleaned_data.get("date_reservation")
        today = date.today()

        if date_reserved < today:
            raise ValidationError("Дата бронирования не может быть раньше сегодняшнего дня")

        return date_reserved


class TableForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования столиков"""

    class Meta:
        model = Table
        fields = "__all__"
