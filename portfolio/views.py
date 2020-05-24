# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt




def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-folios/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'all-folios/search.html',{"message":message})

