from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('mailing:main')


class UsersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'
    extra_context = {
        'title': 'Список пользователей'
    }


class UsersUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    permission_required = 'users.change_user'
    fields = ['first_name', 'last_name', 'email', 'is_active']
    success_url = reverse_lazy('users:list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }
