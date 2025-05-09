from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Property

User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class PropertyModelTestCase(TestCase):

    def setUp(self):
        """Create a user and authenticate API client"""
        self.user = User.objects.create_user(username='testuser', password='TestPass123')
        self.client = APIClient()
        token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_create_property_with_valid_data(self):
        """Test creating a property with valid data"""
        property_data = {
            'address': '123 Main St',
            'postcode': '12345',
            'city': 'Test City',
            'num_rooms': 3,
        }
        response = self.client.post('/api/properties/', property_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(Property.objects.get().address, '123 Main St')

    def test_create_property_without_address(self):
        """Test creating a property without an address should raise an error"""
        property_data = {
            'postcode': '12345',
            'city': 'Test City',
            'num_rooms': 3,
        }
        response = self.client.post('/api/properties/', property_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_all_properties(self):
        """Test viewing all properties"""
        Property.objects.create(address='123 Main St', postcode='12345', city='Test City', num_rooms=3, created_by=self.user)
        Property.objects.create(address='456 Elm St', postcode='67890', city='Other City', num_rooms=2, created_by=self.user)
        
        response = self.client.get('/api/properties/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_view_single_property(self):
        """Test viewing a single property by ID"""
        property = Property.objects.create(address='123 Main St', postcode='12345', city='Test City', num_rooms=3, created_by=self.user)
        
        response = self.client.get(f'/api/properties/{property.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['address'], '123 Main St')

    def test_view_property_with_invalid_id(self):
        """Test viewing a property with an invalid ID (non-existent)"""
        response = self.client.get('/api/properties/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_property(self):
        """Test deleting a property"""
        property = Property.objects.create(address='123 Main St', postcode='12345', city='Test City', num_rooms=3, created_by=self.user)
        
        response = self.client.delete(f'/api/properties/{property.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Property.objects.count(), 0)

    def test_delete_property_with_invalid_id(self):
        """Test deleting a property with an invalid ID (non-existent)"""
        response = self.client.delete('/api/properties/999/')  # ID 999 does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user_cannot_create_property(self):
        """Test that an unauthenticated user cannot create a property"""
        unauthenticated_client = APIClient()
        property_data = {
            'address': '789 Unauthorized St',
            'postcode': '54321',
            'city': 'No Access City',
            'num_rooms': 4,
        }
        response = unauthenticated_client.post('/api/properties/', property_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_cannot_delete_property(self):
        """Test that an unauthenticated user cannot delete a property"""
        # First, create property as authenticated user
        property = Property.objects.create(
            address='Delete Me St',
            postcode='54321',
            city='No Access City',
            num_rooms=4,
            created_by=self.user
        )
        unauthenticated_client = APIClient()
        response = unauthenticated_client.delete(f'/api/properties/{property.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
