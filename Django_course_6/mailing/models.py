from django.db import models

from clients.models import Client
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    TO_BE_SENT = 'Подготовлено'
    SHIPPED = 'Отправлено'

    STATUS_CHOICES = [
        (TO_BE_SENT, "Подготовлено"),
        (SHIPPED, "Отправлено"),
    ]
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=TO_BE_SENT, verbose_name='статус отправки')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )

    start_time = models.TimeField(verbose_name='начало рассылки', **NULLABLE)
    end_time = models.TimeField(verbose_name='конец рассылки', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIODS, default=PERIOD_DAILY,
                              verbose_name='периодичность рассылки')
    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_STARTED, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиенты рассылки')
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель рассылки', **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.users} {self.period} {self.start_time} {self.message} {self.client}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Отправлено'),
        (STATUS_FAILED, 'Ошибка отправки'),
    )

    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время рассылки')
    status = models.CharField(choices=STATUSES, verbose_name='статус попытки')
    clients = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='клиент рассылки', **NULLABLE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
