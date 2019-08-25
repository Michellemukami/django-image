

import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Location,Category,Image
from django.shortcuts import render,redirect


# Create your views here.
def location(request,):
    date = dt.date.today()
    pixels = Image.location()
    return render(request, 'pixel.html', {"date": date,"pixels":pixels})

def mombasa(request):
    date = dt.date.today()
    pixels = Image.objects.filter(Location=3)
    return render(request, 'locations/mombasa.html', {"date": date,"pixels":pixels})

def nakuru(request):
    date = dt.date.today()
    pixels = Image.objects.filter(Location=1)
    return render(request, 'locations/nakuru.html', {"date": date,"pixels":pixels})

def kisii(request):
    date = dt.date.today()
    pixels = Image.objects.filter(Location=2)
    return render(request, 'locations/kisii.html', {"date": date,"pixels":pixels})
def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get("category")
        searched_images=Image.search_by_cat(search_term)
        message = f"{search_term}"

        return render(request, 'locations/search.html',{"message":message, "pixels": searched_images})
    else:
        message="Type in a category to search"
        return render(request, 'locations/search.html',{"message":message})