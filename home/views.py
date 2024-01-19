from django.http import Http404
from django.shortcuts import render
from .models import Artwork, Exhibition, Artwork_Exhibition_Curator
from users.models import User
from django.db.models import Q

def home_page(request):
    exhibitions = Exhibition.objects.all().values()
    arts = Artwork.objects.filter(Q(artwork_id=1) | Q(artwork_id=2) | Q(artwork_id=3))
    context = {
        'exhibitions' : exhibitions,
        'arts' : arts,
    }
    return render(request, 'Home.html', context=context)


def artwork_page(request):
    arts = Artwork.objects.all()
    arts_limit = Artwork.objects.all()[:5]
    artist = User.objects.filter(is_artist=1)
    context = {
        'arts' : arts,
        'arts_limit': arts_limit,
        'artist': artist,
    }
    return render(request, 'Arts.html', context=context)


def artwork_detail(request, id):
    artwork = Artwork.objects.get(artwork_id=id)
    ob = Artwork_Exhibition_Curator.objects.all()
    arts_limit = Artwork.objects.all()[:5]
    arts = Artwork.objects.all()

    if artwork is not None:
        return render(request, 'art-disc.html', context={'artwork' : artwork, 'ob' : ob, 'arts' : arts, 'arts_limit' : arts_limit})
    
    else: 
        raise Http404('artwork not exist')
    
def about_us(request):
    arts_limit = Artwork.objects.all()[:5]
    
    context = {
        'arts_limit' : arts_limit,
    }

    return render(request, 'about.html', context=context)


def exhibition_detail(request, id):
    ob = Exhibition.objects.get(exhibition_id=id)

    if ob is not None:
        return render(request, 'test2.html', context={'exhibition' : ob})
    
    else: 
        raise Http404('Exhibition not exist')