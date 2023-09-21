from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    commentary = models.TextField(verbose_name='комментарий')
    email = models.EmailField(verbose_name='email', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


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
        (STATUS_CREATED, 'Запущена'),
        (STATUS_STARTED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    start_time = models.TimeField(verbose_name='начало рассылки', **NULLABLE)
    end_time = models.TimeField(verbose_name='конец рассылки', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIODS, default=PERIOD_DAILY,
                              verbose_name='периодичность рассылки')
    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_STARTED, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиенты рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return self.status

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

    data_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время рассылки')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    status = models.CharField(max_length=50, choices=STATUSES, verbose_name='статус отправки')
    settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='настройка', **NULLABLE)
    answer = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
