from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import MailingSettingsListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView, MailingSettingsDetailView, LogsListView, index

app_name = MailingConfig.name


urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='list'),
    path('main/', index, name='main'),
    path('create/', MailingSettingsCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', MailingSettingsDetailView.as_view(), name='view'),
    path('logs/', LogsListView.as_view(), name='logs'),

]