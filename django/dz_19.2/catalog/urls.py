from django.urls import path

from catalog.views import index, views_contacts

app_name = 'catalog'

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', views_contacts, name='contacts')
]

