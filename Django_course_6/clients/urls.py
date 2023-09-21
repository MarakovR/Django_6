from django.urls import path
from clients.views import (ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView,
                                ClientsDetailView)

from clients.apps import ClientsConfig

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientsListView.as_view(), name='list'),
    path('clients_create/', ClientsCreateView.as_view(), name='create'),
    path('clients_edit/<int:pk>/', ClientsUpdateView.as_view(), name='edit'),
    path('clients_delete/<int:pk>/', ClientsDeleteView.as_view(), name='delete'),
    path('clients_view/<int:pk>/', ClientsDetailView.as_view(), name='view'),
]