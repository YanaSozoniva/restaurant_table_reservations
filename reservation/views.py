from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from config.settings import EMAIL_HOST_USER

from reservation.forms import ContactForm


class HomeViews(TemplateView):
    """Контроллер для отображения главной страница сайта"""

    form_class = ContactForm
    template_name = "reservation/home.html"

    def get_context_data(self, **kwargs):
        """ Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        """ Обработка post запроса и отправки сообщения менеджеру на почту """

        form = self.form_class(request.POST)
        if form.is_valid():
            name = self.request.POST.get("name")
            message = self.request.POST.get("message")
            phone = self.request.POST.get("phone")
            email = self.request.POST.get("email")
            send_mail(
                subject="Обратная связь",
                message=f"Здравствуйте, Вам пришло сообщение с сайта ресторана (с формы обратной связи). Имя отправителя {name}, "
                        f"сообщение: {message}. Связаться можно по тел.: {phone} или почте: {email}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[EMAIL_HOST_USER],
            )
            messages.success(self.request, "Ваше сообщение отправлено менеджеру. В ближайшее время с Вами свяжутся")
            return redirect('reservation:home')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

