from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    """
    Represents a person model with various details.

    Attributes:
        name (CharField): The name of the person.
        dob (DateField): The date of birth of the person (nullable and optional).
        email (EmailField): The email address of the person (nullable and optional).
        phone_number (PhoneNumberField): The phone number of the person.
        profile_picture (ImageField): The profile picture of the person (nullable and optional).
        person_address (OneToOneField): A one-to-one relationship with the Address model for the person's address (nullable and optional).
    """
    name = models.CharField(max_length=100)

