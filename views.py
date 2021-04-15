from django.shortcuts import render

from travello.models import Destination


def index(request):
    destinations = Destination.objects.all()
    #You should have these images in the 'images' folder located within 'static' folder




    return render(request, 'index.html', {'destinations':destinations})