from django.contrib import admin

from clients.models import Client
from mailing.models import Message, MailingSettings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'text',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('status', 'start_time', 'end_time',)
