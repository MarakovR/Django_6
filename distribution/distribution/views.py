from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from distribution.models import MailingSettings, Logs, Service_client


class MailingSettingsListView(ListView):
    model = MailingSettings
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = ['start_time', 'end_time', 'period', 'status', 'client', ]
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Создание рассылки'
    }


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    fields = ['start_time', 'end_time', 'period', 'status', 'client', ]
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_success_url(self):
        return reverse('mailing:view', args=[self.object.pk])


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class MailingSettingsDetailView(DetailView):
    model = MailingSettings
    extra_context = {
        'title': 'Подробная информация о рассылке'
    }


class LogsListView(ListView):
    model = Logs
    extra_context = {
        'title': 'Логи рассылок'
    }


class Service_clientListView(ListView):
    model = Service_client
    extra_context = {
        'title': 'Список пользователей'
    }


class Service_clientCreateView(CreateView):
    model = Service_client
    fields = ['name', 'email', 'commentary', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Создание пользователя'
    }


class Service_clientUpdateView(UpdateView):
    model = Service_client
    fields = ['email', 'name', 'comment', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }

    def get_success_url(self):
        return reverse('clients:view', args=[self.object.pk])


class Service_clientDeleteView(DeleteView):
    model = Service_client
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


class Service_clientDetailView(DetailView):
    model = Service_client
    extra_context = {
        'title': 'Подробная информация о пользователе'
    }