from django.urls import path
from distribution.views import (MailingSettingsListView, MailingSettingsCreateView, MailingSettingsUpdateView,
                                MailingSettingsDeleteView, MailingSettingsDetailView, LogsListView, Service_clientListView,
                                Service_clientCreateView, Service_clientUpdateView, Service_clientDeleteView,
                                Service_clientDetailView)
from distribution.apps import DistributionConfig

app_name = DistributionConfig.name


urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='list'),
    path('create/', MailingSettingsCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', MailingSettingsDetailView.as_view(), name='view'),
    path('logs/', LogsListView.as_view(), name='logs'),
    path('', Service_clientListView.as_view(), name='list'),
    path('clients_create/', Service_clientCreateView.as_view(), name='create'),
    path('clients_edit/<int:pk>/', Service_clientUpdateView.as_view(), name='edit'),
    path('clients_delete/<int:pk>/', Service_clientDeleteView.as_view(), name='delete'),
    path('clients_view/<int:pk>/', Service_clientDetailView.as_view(), name='view'),
]