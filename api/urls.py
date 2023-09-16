from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView

# Create a router for PersonViewSet
urlpatterns = [
    path('/api', PersonListCreateView.as_view(), name='person-list-create'),
    path('/api/<int:id>', PersonRetrieveUpdateDeleteView.as_view(), name='person-retrieve-update-delete'),
]