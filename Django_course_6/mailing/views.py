from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from clients.models import Client
from mailing.models import MailingSettings, Logs


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings

    extra_context = {
        'title': 'Список рассылок'
    }


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = ['start_time', 'end_time', 'period', 'status', 'client', 'users']
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Создание рассылки'
    }


class MailingSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingSettings
    permission_required = 'mailing.change_mailingsettings'
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


def index(request):
    count_mailing = len(MailingSettings.objects.all())
    mailing_activ = len(MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED))
    count_clients = len(Client.objects.all())
    context = {
        'title': 'Главная',
        'count_mailing': count_mailing,
        'mailing_activ': mailing_activ,
        'count_clients': count_clients,

    }
    return render(request, 'mailing/main.html', context)
