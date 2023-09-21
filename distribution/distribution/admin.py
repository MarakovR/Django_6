from django.contrib import admin
from distribution.models import Service_client, Message, MailingSettings, Logs


@admin.register(Service_client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'text',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('status', 'message', 'start_time', 'end_time', )


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'answer',)
