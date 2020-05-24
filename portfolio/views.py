# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

from .models import *

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# displaying different photo categories in cards
def photo_category(request):
    date = dt.date.today()## current date
    portfolio = Image.objects.all
    return render(request, 'all-folios/category.html', {"date": date, "portfolio": portfolio})

def about(request):
    date = dt.date.today()
    return render(request, 'all-folios/about.html', {"date": date,})


## added this
def contact(request):
    date = dt.date.today()
    return render(request, 'all-folios/contact.html', {"date": date,})




def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-folios/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'all-folios/search.html',{"message":message})

