from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateView, HabitUpdateView, HabitRetrieveView, HabitDestroyView, HabitListView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitRetrieveView.as_view(), name='habit-detail'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(), name='habit-delete'),
    path('', HabitListView.as_view(), name='habit-list'),
]
