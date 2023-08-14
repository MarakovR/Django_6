from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def views_contacts(request):
    return render(request, 'catalog/contacts.html')
