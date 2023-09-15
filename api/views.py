from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    """
    Provides endpoints for listing all persons and creating a new person.

    Attributes:
        queryset (QuerySet): The queryset containing all Person objects.
        serializer_class (Serializer): The serializer class for Person objects.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides endpoints for retrieving, updating, and deleting a person.

    Attributes:
        queryset (QuerySet): The queryset containing all Person objects.
        serializer_class (Serializer): The serializer class for Person objects.
        lookup_field (str): The field used to look up a person, which is 'name' in this case.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'
