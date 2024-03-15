from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message

from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def check_and_send_daily_reminders():
    """Отправляет напоминания о ежедневных привычках пользователям через Telegram."""
    daily_habits = Habit.objects.filter(is_pleasant=False, frequency='day')

    for habit in daily_habits:
        _send_habit_reminder(habit)


@shared_task
def check_and_send_weekly_reminders():
    """Отправляет напоминания о еженедельных привычках пользователям через Telegram."""

    weekly_habits = Habit.objects.filter(is_pleasant=False, frequency='week')

    for habit in weekly_habits:
        _send_habit_reminder(habit)


def _send_habit_reminder(habit):
    """Функция отправки напоминания."""
    if habit.user.telegram:
        chat_id = habit.user.telegram
        message = f"Напоминание: {habit.action} в {habit.location} в {habit.time.strftime('%H:%M')}"
        if habit.reward:
            message += f" Награда за выполнение: {habit.reward}."
        if habit.linked_habit:
            linked_habit_action = habit.linked_habit.action
            message += f" Связанная привычка: {linked_habit_action}."
        send_telegram_message(chat_id, message)
