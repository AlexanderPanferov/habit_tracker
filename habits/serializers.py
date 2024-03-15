from rest_framework import serializers

from habits.models import Habit


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
