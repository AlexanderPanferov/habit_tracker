from rest_framework import serializers

from habits.models import Habit


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
