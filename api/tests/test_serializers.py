from django.test import TestCase
from api.models import Person
from api.serializers import PersonSerializer

class PersonSerializerTests(TestCase):
    def setUp(self):
        # Create a Person instance for testing
        self.person_data = {
            'name': 'John Doe',
            'phone_number': '+1234567890'
        }
        self.person = Person.objects.create(**self.person_data)

    def test_serializer_valid_data(self):
        serializer = PersonSerializer(instance=self.person)
        expected_data = {
            'id': self.person.id,
            'name': 'John Doe',
            'dob': None,
            'email': None,
            'phone_number': '+1234567890'
        }
        self.assertEqual(serializer.data, expected_data)

    def test_serializer_invalid_data(self):
        # Test serializer with invalid data (missing required field 'name')
        invalid_data = {'phone_number': '+1234567890'}
        serializer = PersonSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_create(self):
        # Test serializer create with valid data
        valid_data = {
            'name': 'Jane Smith',
            'phone_number': '+9876543210'
        }
        serializer = PersonSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        new_person = serializer.save()
        self.assertEqual(new_person.name, 'Jane Smith')

    def test_serializer_update(self):
        # Test serializer update with valid data
        valid_data = {
            'name': 'Updated Name',
            'phone_number': '+1234567890'
        }
        serializer = PersonSerializer(instance=self.person, data=valid_data)
        self.assertTrue(serializer.is_valid())
        updated_person = serializer.save()
        self.assertEqual(updated_person.name, 'Updated Name')
