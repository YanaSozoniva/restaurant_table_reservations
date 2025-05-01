from django.forms import BooleanField

from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class StyleFormMixin:
    """Стилизация форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """ Форма регистрации пользователя """
    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_name", "password1", "password2")


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    """ Форма изменения профиля пользователя """
    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_name", )
