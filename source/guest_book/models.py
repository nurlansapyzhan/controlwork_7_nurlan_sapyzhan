from django.db import models

# Create your models here.
STATUS_TYPES = (('active', 'Активно'), ('blocked', 'Заблокировано'))


class Book(models.Model):
    author = models.CharField(max_length=30, null=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=254, null=False, verbose_name='Почта автора записи')
    text = models.TextField(null=False, verbose_name='Текст записи')
    created_date = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_date = models.DateTimeField(auto_now=False, verbose_name='Время редактирования', null=True)
    status = models.CharField(max_length=50, null=False, choices=STATUS_TYPES, default=STATUS_TYPES[0][0], verbose_name='Статус')
