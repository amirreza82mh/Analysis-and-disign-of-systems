from django.http import Http404
from django.shortcuts import render
from .models import Artwork, Exhibition 

def artwork_detail(request, id):
    ob = Artwork.objects.get(artwork_id=id)
    if ob is not None:
        return render(request, 'test1.html', context={'Artwork' : ob})
    else: 
        raise Http404('artwork not exist')
    
def exhibition_detail(request, id):
    ob = Exhibition.objects.get(exhibition_id=id)
    if ob is not None:
        return render(request, 'test2.html', context={'exhibition' : ob})
    else: 
        raise Http404('Exhibition not exist')