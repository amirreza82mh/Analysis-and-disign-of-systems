from django.http import Http404
from django.shortcuts import render, redirect
from .models import Artwork, Exhibition, Artwork_Exhibition_Curator, Contact
from .forms import ContactForm
from users.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


def contact_us(request):
    arts_limit = Artwork.objects.all()[:5]

    if request.method == 'POST':
        form = ContactForm(request.POST)
    
        if form.is_valid():
            info = form.cleaned_data

            try:
                info[request.POST.get('type')] = True
                Contact.objects.create(first_last_name=info['first_last_name'], email=info['email'], subject=info['subject'], text=info['text'])
                messages.success(request, 'User successfully SignUp', extra_tags="success")
                return redirect('contact_us_page')
            
            except Exception as error:
                    messages.error(request, error, extra_tags="danger")
                    return redirect('contact_us_page')
            
        else:
            messages.error(request, form.errors, extra_tags="danger")
            return redirect('contact_us_page')
    
    else:
        form = ContactForm()

        context= {
            'arts_limit' : arts_limit,
            'form' : form
        }

    return render(request, 'contact.html', context=context)

@login_required(login_url='login_view')
def reserve_ticket(request, id):
    arts_limit = Artwork.objects.all()[:5]
    exhibition = Exhibition.objects.get(exhibition_id=id)

    context={
        'exhibition' : exhibition,
        'arts_limit' : arts_limit
    }

    if exhibition is not None:
        return render(request, 'reserve-ticket.html', context=context)
    
    else: 
        raise Http404('Exhibition not exist')