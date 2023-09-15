from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView

# Create a router for PersonViewSet
urlpatterns = [
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('<int:id>/', PersonRetrieveUpdateDeleteView.as_view(), name='person-retrieve-update-delete'),
]