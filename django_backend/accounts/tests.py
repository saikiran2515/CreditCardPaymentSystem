from django.test import TestCase
from django.contrib.auth.models import User


class UserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            password="test123"
        )

        self.assertEqual(user.username, "testuser")

    def test_user_exists(self):
        User.objects.create_user(
            username="sai",
            password="pass123"
        )

        self.assertEqual(User.objects.count(), 1)

    def test_password_check(self):
        user = User.objects.create_user(
            username="kiran",
            password="secret123"
        )

        self.assertTrue(user.check_password("secret123"))