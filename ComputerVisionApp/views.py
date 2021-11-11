from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        context = {
            'title': "Welcome to Car Checker"
        }
        return render(request, 'index.html', context)
