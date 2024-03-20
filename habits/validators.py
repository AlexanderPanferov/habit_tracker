from django.core.exceptions import ValidationError
from datetime import timedelta


def habit_validator(value):
    """ Проверка на правильность заполнения полей привычки """

    max_duration = timedelta(minutes=2)

    if value.get('is_pleasant'):
        if value.get('linked_habit') or value.get('reward'):
            raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')

    if value.get("linked_habit") and value.get("reward"):
        raise ValidationError('Можно выбрать или связанную привычку или вознаграждение')

    if value.get('duration', timedelta()) > max_duration:
        raise ValidationError('Привычку можно выполнять не более 2 минут')

    if value.get("linked_habit"):
        if not value.get("linked_habit").is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только приятные привычки')
