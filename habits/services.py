import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    """Функция для отправки сообщений в телеграмм"""
    url = "https://api.telegram.org/bot"
    token = settings.TELEGRAM_API_KEY

    requests.post(
        url=f"{url}{token}/sendMessage",
        data={
            'chat_id': chat_id,
            'text': message,
        }
    )
