import secrets

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserCreateViews(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Здравствуйте, для регистрации почты {url} перейдите по ссылке",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        messages.success(self.request, "Письмо с подтверждением отправлено на ваш email.")
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.token = None
    user.is_active = True
    user.save()
    messages.success(request, "Ваш email успешно подтверждён!")
    return redirect(reverse("users:login"))


class UserUpdateViews(LoginRequiredMixin, UpdateView):
    template_name = "users/register.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:login")

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse("users:user_detail", args=[self.kwargs.get("pk")])


class UserDetail(DetailView):
    """Контроллер вывода списка сообщений"""

    model = User
    template_name = "users/user_detail.html"
    context_object_name = "user"
