from django.test import TestCase
from api.models import Person
from django.core.exceptions import ValidationError

class PersonModelTest(TestCase):
    def test_person_creation(self):
        person = Person.objects.create(
            name='John Doe',
            phone_number='+1234567890'
        )
        self.assertEqual(str(person), 'John Doe')
        self.assertEqual(person.phone_number, '+1234567890')

    def test_person_creation_with_optional_fields(self):
        person = Person.objects.create(
            name='Jane Doe',
            phone_number='+9876543210',
            dob='1990-01-01',
            email='jane@example.com'
        )
        self.assertEqual(person.dob, '1990-01-01')
        self.assertEqual(person.email, 'jane@example.com')

    def test_invalid_phone_number(self):
        with self.assertRaises(ValidationError):
            # This should raise a validation error due to an invalid phone number
            Person.objects.create(
                name='Invalid Person',
                phone_number='123456'  # Invalid phone number
            )
