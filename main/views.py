from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def booking(request):
    return render(request, 'main/booking.html')


