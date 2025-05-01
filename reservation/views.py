from django.views.generic import TemplateView

from reservation.forms import ContactForm


class HomeViews(TemplateView):
    """Контроллер для отображения главной страница сайта"""

    form_class = ContactForm
    template_name = "reservation/home.html"
