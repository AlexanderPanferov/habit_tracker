from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitRetrieveView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
