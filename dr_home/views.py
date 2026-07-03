from django.shortcuts import render


def dr_home(request):
    # Simple page that reuses the main/home template for now.
    return render(request, 'main/home.html')

