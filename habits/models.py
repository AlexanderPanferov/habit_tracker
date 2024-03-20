from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD_CHOICES = [
        ('week', 'еженедельно'),
        ('day', 'ежедневно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    name = models.CharField(max_length=50, verbose_name='Название')
    location = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                     limit_choices_to={'is_pleasant': True}, verbose_name='Связанная привычка')
    frequency = models.CharField(max_length=15, choices=PERIOD_CHOICES, default='day', verbose_name='Переодичность')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Вознаграждение')
    duration = models.DurationField(verbose_name="Время на выполнение", help_text="Не больше 120 секунд")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
