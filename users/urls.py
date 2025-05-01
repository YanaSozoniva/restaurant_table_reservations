from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetView)
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import UserCreateViews, UserUpdateViews, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateViews.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("users/<int:pk>/update", UserUpdateViews.as_view(), name="user_update"),
]
