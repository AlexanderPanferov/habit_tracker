from rest_framework.serializers import ValidationError
from datetime import timedelta


def habit_validator(value):
    """ Проверка на правильность заполнения полей привычки """

    max_duration = timedelta(minutes=2)

    if value['is_pleasant']:
        if value['linked_habit'] or value['reward']:
            raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')

    if value["linked_habit"] and value["reward"]:
        raise ValidationError('Можно выбрать или связанную привычку или вознаграждение')

    if value['duration'] > max_duration:
        raise ValidationError('Привычку можно выполнять не более 2 минут')

    if value["linked_habit"]:
        if not value["linked_habit"].is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только приятные привычки')
