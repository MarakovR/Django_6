from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    commentary = models.TextField(verbose_name='комментарий')
    email = models.EmailField(verbose_name='email', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'