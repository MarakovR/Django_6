from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from mailing.models import MailingSettings


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
