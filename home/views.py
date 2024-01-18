from django.http import Http404
from django.shortcuts import render
from .models import Artwork

def home_page(request):
    return render(request, 'Home.html')

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')    

def artwork_detail(request, id):
    ob = Artwork.objects.get(artwork_id=id)
    if ob is not None:
        return render(request, 'test.html', context={'Artwork' : ob})
    else: 
        raise Http404('artwork not exist')