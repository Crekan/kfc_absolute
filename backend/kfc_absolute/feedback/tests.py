from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from .models import Feedback


class FeedbackAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            full_name='test_full_name',
            password='test_password',
            repeat_password='test_password',
        )
        self.client.login(
            username='test_username',
            password='test_password',
        )
        self.feedback_data = {
            'address': 'жалоба',
            'team': 'Весь управляющий состав (зам. директора и директор)',
            'situation': 'Некоторая ситуация',
        }
        self.invalid_feedback_data = {
            'address': 'жалоба',
            'team': 'Весь управляющий состав (зам. директора и директор)',
            'situation': 'Некоторая ситуация',
            'other': 'a',
        }
        self.feedback = Feedback.objects.create(**self.feedback_data)

    def test_create_feedback(self):
        url = reverse('feedback_create')
        response = self.client.post(url, data=self.feedback_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 2)

    def test_create_invalid_feedback(self):
        url = reverse('feedback_create')
        response = self.client.post(url, data=self.invalid_feedback_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Feedback.objects.count(), 1)

    def test_list_feedback(self):
        url = reverse('feedback_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
