from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='mail@mail.com')
        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            'user': self.user.pk,
            'name': 'Test',
            'location': 'Test',
            'time': '10:10:10',
            'action': 'Test',
            'frequency': 'day',
            'duration': '50',
        }

        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'Test', 'location': 'Test', 'time': '10:10:10', 'action': 'Test', 'is_pleasant': False,
             'frequency': 'day', 'reward': None, 'duration': 50, 'is_public': False, 'user': 1, 'linked_habit': None}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """Тестирование списка привычек"""
        habit = Habit.objects.create(
            user=self.user,
            name='Test1',
            location='Test',
            time='10:10:10',
            action='Test',
            frequency='day',
            duration='50',
        )

        response = self.client.get(
            reverse('habits:habit-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': habit.pk, 'name': 'Test1', 'location': 'Test', 'time': '10:10:10', 'action': 'Test',
                 'is_pleasant': False, 'frequency': 'day', 'reward': None, 'duration': 50, 'is_public': False,
                 'user': self.user.pk, 'linked_habit': None}]}
        )

    def test_detail_habit(self):
        """Тестирование просмотра привычек"""
        habit = Habit.objects.create(
            user=self.user,
            name='Test1',
            location='Test',
            time='10:10:10',
            action='Test',
            frequency='day',
            duration='50',
        )

        response = self.client.get(
            reverse('habits:habit-detail', kwargs={'pk': habit.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': habit.pk, 'name': 'Test1', 'location': 'Test', 'time': '10:10:10', 'action': 'Test', 'is_pleasant': False,
             'frequency': 'day', 'reward': None, 'duration': 50, 'is_public': False, 'user': self.user.pk, 'linked_habit': None}

        )

    def test_update_habit(self):
        """Тестирование обнавления привычки"""
        habit = Habit.objects.create(
            user=self.user,
            name='Test1',
            location='Test',
            time='10:10:10',
            action='Test',
            frequency='day',
            duration='50',
        )

        data = {
            'time': '11:11:11'
        }

        response = self.client.patch(
            reverse('habits:habit-update', kwargs={'pk': habit.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': habit.pk, 'name': 'Test1', 'location': 'Test', 'time': '11:11:11', 'action': 'Test', 'is_pleasant': False,
             'frequency': 'day', 'reward': None, 'duration': 50, 'is_public': False, 'user': self.user.pk, 'linked_habit': None}

        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        habit = Habit.objects.create(
            user=self.user,
            name='Test1',
            location='Test',
            time='10:10:10',
            action='Test',
            frequency='day',
            duration='50',
        )

        response = self.client.delete(
            reverse('habits:habit-delete', kwargs={'pk': habit.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
