from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Person model.

    This serializer is used to convert Person model instances into JSON data and vice versa.
    It includes all fields of the Person model, including a nested AddressSerializer.

    Attributes:
        model: The model class that this serializer is based on (Person).
        fields: A list of fields to include in the serialized representation. Here, '__all__' includes all fields.
    """
    class Meta:
        model = Person
        fields = '__all__'
