from django.shortcuts import render


def dr_home(request):
    return render(request, 'main/home.html')

