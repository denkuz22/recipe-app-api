"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # def test_new_user_email_normalized(self):
    #     """Test email is normalized for new users."""
    #     sample_emails = [
    #         ['XXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXX'],
    #         ['XXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXX'],
    #         ['XXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXX'],
    #         ['XXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXX'],
    #     ]
    #     for email, expected in sample_emails:
    #         user = get_user_model().objects.create_user(email, 'sample123')