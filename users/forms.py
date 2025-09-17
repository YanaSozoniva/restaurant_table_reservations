from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    """Стилизация форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
            if field_name == "phone":
                field.widget.attrs.update({"placeholder": "+7 (XXX) XXX-XX-XX"})
            if field_name == "date_reservation":
                field.widget = forms.DateInput(
                    attrs={
                        "type": "date",
                        "class": "form-control datepicker",
                        "min": datetime.now().strftime("%Y-%m-%d"),
                    },
                    format="%Y-%m-%d",
                )
            if field_name == "time_reservation":
                field.widget = forms.TimeInput(
                    attrs={
                        "type": "time",
                        "class": "form-control timepicker",
                        "step": "300",
                        "min": "10:00",  # Минимальное время
                        "max": "23:00",  # Максимальное время
                    }
                )


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""

    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_name", "password1", "password2")


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    """Форма изменения профиля пользователя"""

    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_name", "last_name", "first_name")
