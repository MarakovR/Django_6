# Generated by Django 4.2.5 on 2023-10-01 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("theme", models.CharField(max_length=100, verbose_name="тема письма")),
                ("text", models.TextField(verbose_name="текст")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Подготовлено", "Подготовлено"),
                            ("Отправлено", "Отправлено"),
                        ],
                        default="Подготовлено",
                        max_length=50,
                        verbose_name="статус отправки",
                    ),
                ),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
            },
        ),
        migrations.CreateModel(
            name="MailingSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="начало рассылки"
                    ),
                ),
                (
                    "end_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="конец рассылки"
                    ),
                ),
                (
                    "period",
                    models.CharField(
                        choices=[
                            ("daily", "Ежедневная"),
                            ("weekly", "Раз в неделю"),
                            ("monthly", "Раз в месяц"),
                        ],
                        default="daily",
                        max_length=50,
                        verbose_name="периодичность рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("started", "Запущена"),
                            ("done", "Завершена"),
                        ],
                        default="started",
                        max_length=50,
                        verbose_name="статус рассылки",
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(
                        to="clients.client", verbose_name="клиенты рассылки"
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.message",
                        verbose_name="сообщение",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время рассылки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ok", "Отправлено"), ("failed", "Ошибка отправки")],
                        verbose_name="статус попытки",
                    ),
                ),
                (
                    "clients",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="clients.client",
                        verbose_name="клиент рассылки",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailingsettings",
                        verbose_name="рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "лог",
                "verbose_name_plural": "логи",
            },
        ),
    ]
