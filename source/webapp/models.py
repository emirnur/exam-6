from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class HostBook(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Статус', default=STATUS_CHOICES[0][0],
                                choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

