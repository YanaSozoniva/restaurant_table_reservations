from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView, DetailView

from reservation.forms import EmployeeForm
from reservation.services import get_statistical_data
from reservation.models import Restaurant, Employee


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
    template_name = "admin/employee_form.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    """Контроллер удаления сотрудника"""

    model = Employee
    form_class = EmployeeForm
    template_name = "admin/employee_delete.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер изменения сотрудников"""

    model = Employee
    form_class = EmployeeForm
    template_name = "admin/employee_form.html"
    success_url = reverse_lazy("admin_page:employee_list")


class EmployeeDetail(DetailView):
    """Контроллер детализации сотрудников"""

    model = Employee
    template_name = "admin/employee_detail.html"

