from django.shortcuts import render


# Mettre le docstring
def index(request):
    return render(request, 'index.html')
