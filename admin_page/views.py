from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView, DetailView
from django.shortcuts import get_object_or_404, redirect

from reservation.forms import EmployeeForm, RestaurantForm
from reservation.services import get_statistical_data
from reservation.models import Restaurant, Employee
from users.models import User


class AdminPageViews(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """Контроллер для отображения страница для администратора сайта"""

    template_name = "admin_page/admin_page.html"
    permission_required = "users.can_change_content"

    def get_context_data(self, **kwargs):
        """Статистические данные"""
        context = super().get_context_data(**kwargs)

        context["data"] = get_statistical_data()
        return context


class EmployeeCreate(LoginRequiredMixin, CreateView):
    """Контроллер создания нового сотрудника"""

    model = Employee
    form_class = EmployeeForm
    template_name = "admin_page/employee_form.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    """Контроллер удаления сотрудника"""

    model = Employee
    form_class = EmployeeForm
    template_name = "admin_page/employee_delete.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер изменения сотрудников"""

    model = Employee
    form_class = EmployeeForm
    template_name = "admin_page/employee_form.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeDetail(DetailView):
    """Контроллер детализации сотрудников"""

    model = Employee
    template_name = "admin_page/employee_detail.html"


class EmployeeList(ListView):
    """Контроллер вывода списка столов"""

    model = Employee
    template_name = "admin_page/employee_list.html"
    context_object_name = "employees"


class RestaurantUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер изменения информации о ресторане"""

    model = Restaurant
    form_class = RestaurantForm
    template_name = "admin_page/restaurant_form.html"

    def get_success_url(self):
        return reverse("admin_page:restaurant_detail", args=[self.kwargs.get("pk")])


class RestaurantDetail(DetailView):
    """Контроллер детализации ресторана"""

    model = Restaurant
    template_name = "admin_page/restaurant_detail.html"
