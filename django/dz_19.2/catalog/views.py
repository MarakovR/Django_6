from django.shortcuts import render


def catalog(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'index.html')
