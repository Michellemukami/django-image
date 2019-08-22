

import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Location,Category,Location
from django.shortcuts import render,redirect


# Create your views here.
def location(request,):
    date = dt.date.today()
    pixels = Location.location
    return render(request, 'pixel.html', {"date": date,"pixels":pixels})

def mombasa(request,name):
    date = dt.date.today()
    pixels = Location.objects.get(name = mombasa)
    return render(request, 'location/mombasa.html', {"date": date,"pixels":pixels})

def nakuru(request,name):
    date = dt.date.today()
    pixels = Location.objects.get(name = nakuru)
    return render(request, 'location/nakuru.html', {"date": date,"pixels":pixels})

def kisii(request,name):
    date = dt.date.today()
    pixels = Location.objects.get(name = kisii)
    return render(request, 'location/kisii.html', {"date": date,"pixels":pixels})
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Pixel.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'locations/search.html',{"message":message,"pixel": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'locations/search.html',{"message":message})

