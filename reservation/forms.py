from datetime import datetime, date

from django.utils import timezone
from django import forms
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField
from reservation.models import Reservation, Table

from users.forms import StyleFormMixin


class ContactForm(StyleFormMixin, forms.Form):
    """ Форма обратной связи """
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator()])
    phone = PhoneNumberField(required=False)
    message = forms.CharField(widget=forms.Textarea)


class ReservationForm(StyleFormMixin, forms.ModelForm):
    """ Форма нового бронирования """
    class Meta:
        model = Reservation
        exclude = ("customer",)

    def clean_date_reservation(self):
        """Валидация проверки даты бронирования столика"""
        cleaned_data = super().clean()
        date_reservation = cleaned_data.get("date_reservation")
        today = date.today()

        if date_reservation < today:
            self.add_error("date_reservation", "Дата бронирования не может быть позже сегодняшней даты")

        return date_reservation

    def clean_time_reservation(self):
        """Валидация проверки время бронирования столика"""
        time_reservation = self.cleaned_data.get("time_reservation")
        now = timezone.now()
        time_plus_2h = (now + timezone.timedelta(hours=2)).time()

        if time_reservation > time_plus_2h:
            self.add_error("time_reservation", "Бронирование доступно за 2 часа до назначенного часа")

        return time_reservation


class TableForm(StyleFormMixin, forms.ModelForm):
    """ Форма для создания и редактирования столиков """
    class Meta:
        model = Table
        fields = '__all__'
