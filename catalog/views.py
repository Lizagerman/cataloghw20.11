from django.shortcuts import render


def index_homepage(request):
    return render(request, 'catalog/templates.home.html')


def contacts(request):
    return render(request, 'catalog/templates.contacts.html')
