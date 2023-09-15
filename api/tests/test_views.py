from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Person
from api.serializers import PersonSerializer

class PersonTests(APITestCase):
    def setUp(self):
        # Create some initial data for testing
        self.person1 = Person.objects.create(name='John Doe', phone_number='+1234567890')
        self.person2 = Person.objects.create(name='Jane Smith', phone_number='+9876543210')

    def test_get_all_persons(self):
        url = reverse('person-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = PersonSerializer([self.person1, self.person2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_person(self):
        url = reverse('person-list-create')
        data = {'name': 'New Person', 'phone_number': '+1111111111'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Person')

    def test_get_person(self):
        url = reverse('person-retrieve-update-delete', kwargs={'id': self.person1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = PersonSerializer(self.person1).data
        self.assertEqual(response.data, expected_data)

    def test_update_person(self):
        url = reverse('person-retrieve-update-delete', kwargs={'id': self.person1.id})
        data = {'name': 'Updated Name', 'phone_number': '+1234567890'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_delete_person(self):
        url = reverse('person-retrieve-update-delete', kwargs={'id': self.person1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Person.DoesNotExist):
            Person.objects.get(id=self.person1.id)
