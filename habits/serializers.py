from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validator


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            habit_validator,
        ]
