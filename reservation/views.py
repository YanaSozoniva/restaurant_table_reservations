from datetime import datetime

from django.contrib import messages
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from config.settings import EMAIL_HOST_USER
from reservation.forms import ContactForm, ReservationForm, TableForm
from reservation.models import Reservation, Table
from reservation.services import get_free_tables
import logging
logger = logging.getLogger(__name__)


class HomeViews(TemplateView):
    """Контроллер для отображения главной страница сайта"""

    form_class = ContactForm
    template_name = "reservation/home.html"

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        """Обработка post запроса и отправки сообщения менеджеру на почту"""

        form = self.form_class(request.POST)
        if form.is_valid():
            name = self.request.POST.get("name")
            message = self.request.POST.get("message")
            phone = self.request.POST.get("phone")
            email = self.request.POST.get("email")
            send_mail(
                subject="Обратная связь",
                message=f"Здравствуйте, Вам пришло сообщение с сайта ресторана (с формы обратной связи). "
                        f"Имя отправителя {name}, сообщение: {message}. "
                        f"Связаться можно по тел.: {phone} или почте: {email}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[EMAIL_HOST_USER],
            )
            messages.success(self.request, "Ваше сообщение отправлено менеджеру. В ближайшее время с Вами свяжутся")
            return redirect("reservation:home")
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class AboutRestaurantViews(TemplateView):
    """Контроллер для отображения главной страница сайта"""

    template_name = "reservation/restaurant.html"


class ReservationCreate(CreateView):
    """Контроллер нового бронирования столика"""

    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/reservation_form.html"
    success_url = reverse_lazy("reservation:reservation_list")

    def form_valid(self, form):
        reservation = form.save()
        user = self.request.user
        reservation.customer = user
        reservation.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tables'] = Table.objects.all()  # Получаем все столики
        return context


@require_GET
def get_available_tables(request):
    """AJAX-функция для получения доступных столиков"""
    logger.debug(f"Получен запрос с параметрами: {request.GET}")
    date_str = request.GET.get('date_reservation')
    time_str = request.GET.get('time_reservation')

    if not date_str or not time_str:
        return JsonResponse({'error': 'Не указана дата или время'}, status=400)

        # Получаем занятые столики на эту дату и время
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M').time()
        available_tables = get_free_tables(date, time)
        tables_data = [{
            'id': table.id,
            'number': table.table_number,
            'capacity': table.table_capacity,
            'location': table.location or "",
        } for table in available_tables]

        return JsonResponse({'tables': tables_data})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


class ReservationDetail(DetailView):
    """Контроллер детализации брони"""

    model = Reservation
    template_name = "reservation/reservation_detail.html"


class ReservationList(ListView):
    """Контроллер вывода списка брони"""

    model = Reservation
    template_name = "reservation/reservation_list.html"
    context_object_name = "reservations"
    ordering = ['date_reservation', 'time_reservation']

    def get_queryset(self):
        """Выборка брони по пользователю"""
        queryset = cache.get('reservations_queryset')
        if not queryset:
            queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user.id)


class ReservationDelete(DeleteView):
    """Контроллер удаления брони"""

    model = Reservation
    template_name = "reservation/reservation_delete.html"
    success_url = reverse_lazy("reservation:reservation_list")


class TableList(ListView):
    """Контроллер вывода списка столов"""

    model = Table
    template_name = "reservation/table_list.html"
    context_object_name = "tables"


class TableDetail(DetailView):
    """Контроллер детализации столов"""

    model = Table
    template_name = "reservation/table_detail.html"


class TableCreate(CreateView):
    """Контроллер создания нового стола"""

    model = Table
    form_class = TableForm
    template_name = "reservation/table_form.html"
    success_url = reverse_lazy("reservation:table_list")


class TableUpdate(UpdateView):
    """Контроллер изменения стола"""

    model = Table
    form_class = TableForm
    template_name = "reservation/table_form.html"
    success_url = reverse_lazy("reservation:table_list")

    def get_success_url(self):
        return reverse("reservation:table_detail", args=[self.kwargs.get("pk")])


class TableDelete(DeleteView):
    """Контроллер удаления столов"""

    model = Table
    template_name = "reservation/table_confirm_delete.html"
    success_url = reverse_lazy("reservation:table_list")
