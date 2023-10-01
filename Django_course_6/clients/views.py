from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from clients.models import Client


class ClientsListView(ListView):
    model = Client
    extra_context = {
        'title': 'Список пользователей'
    }


class ClientsCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'commentary', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Создание клиента рассылки'
    }


class ClientsUpdateView(UpdateView):
    model = Client
    fields = ['email', 'name', 'commentary', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }

    def get_success_url(self):
        return reverse('clients:view', args=[self.object.pk])


class ClientsDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


class ClientsDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Подробная информация о пользователе'
    }