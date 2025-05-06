from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class UserModelTestCase(TestCase):

    def test_create_user_with_valid_data(self):
        """Test creating a user with valid data"""
        user = User.objects.create_user(username='testuser', password='TestPass123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('TestPass123'))
        self.assertEqual(user.role, 'normal')

    def test_create_user_with_invalid_role(self):
        """Test creating a user with an invalid role"""
        with self.assertRaises(ValueError):
            User.objects.create_user(username='testuser', password='TestPass123', role='invalid_role')

    def test_create_admin(self):
        """Test creating a user with the default role ('normal')"""
        user = User.objects.create_user(username='adminuser', password='adminPass123', role='admin')
        self.assertEqual(user.username, 'adminuser')
        self.assertEqual(user.role, 'admin')
        self.assertTrue(user.check_password('adminPass123')) 
            
    def test_create_user_with_default_role(self):
        """Test creating a user with the default role ('normal')"""
        user = User.objects.create_user(username='normaluser', password='TestPass123', role='normal')
        self.assertEqual(user.username, 'normaluser')
        self.assertEqual(user.role, 'normal')
        self.assertTrue(user.check_password('TestPass123'))
