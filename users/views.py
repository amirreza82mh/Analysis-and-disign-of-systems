from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UpdateForm, ArtworkForm
from .models import User
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from home.models import Artwork
from django.http import Http404

def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            if info['password1'] != info['password2']:
                messages.error(request, 'please enter same password in field confirmpassword', extra_tags="daner")
                return redirect('signup_view')
                        
            try:
                info[request.POST.get('type')] = True
                User.objects.create(username=info['username'], email=info['email'], phone_number=info['phone_number'], password=make_password(info['password1']), is_curator=info['is_curator'], is_artist=info['is_artist'], is_viewer=info['is_viewer'])
                messages.success(request, 'User successfully SignUp', extra_tags="success")
                return redirect('admin')
            
            except Exception as error:
                messages.error(request, error, extra_tags="danger")
                return render(request, 'login.html')
            
        else:
            messages.error(request, form.errors, extra_tags="danger")
            return redirect('signup_view')
        
    else:
        form = SignUpForm()

    return render(request, 'login.html', context={"form": form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            username = info['username']
            password = info['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_artist:
                login(request=request, user=user)
                messages.success(request, 'login successfull', extra_tags="succuss")
                return redirect('artist_dashboard')
            
            elif user is not None and user.is_viewer:
                login(request=request, user=user)
                messages.success(request, 'login successfull', extra_tags="succuss")
                return redirect('viewer_dashboard')

            elif user is not None and user.is_curator:
                login(request=request, user=user)
                messages.success(request, 'login successfull', extra_tags="succuss")
                return redirect('curator_dashboard')
            
            else:
                messages.error(request, 'invalid credentials', extra_tags="danger")
                return redirect('login_view')
            
        else:
            messages.error(request, 'form is not valid', extra_tags="danger")
            return redirect('login_view')

    else:
        form = LoginForm(request.POST)
    
    return render(request, 'login.html', context={'form': form})


def Update(request):
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            user = User.objects.get(id=request.user.id)
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.email = info['email']
            user.phone_number = info['phone_number']
            user.username = info['username']
            user.save()

            return redirect('home_page')

        else:
            messages.error(request, 'form is not valid', extra_tags="danger")
            return redirect('home_page')
    
    else:
        raise Http404('don not do this')
    

@login_required(login_url='login_view')
def select_dash(request):
    if request.user.is_artist:
        return redirect('artist_dashboard')
            
    elif request.user.is_viewer:
        return redirect('viewer_dashboard')

    elif request.user.is_curator:
        return redirect('curator_dashboard')


@login_required(login_url='login_view')
def viewer_dashboard(request):
    arts_limit = Artwork.objects.all()[:5]
    if request.user.is_viewer:
        return render(request, 'viewer-dash.html', context={'viewer': request.user, 'arts_limit' : arts_limit})
    else:
        raise Http404('access denied!')
    
    
@login_required(login_url='login_view')
def artist_dashboard(request):
    arts_limit = Artwork.objects.all()[:5]
    user_art = Artwork.objects.filter(artist=request.user)
    if request.user.is_artist:
        return render(request, 'artist-dash.html', context={'artist': request.user, 'arts_limit' : arts_limit, 'user_art' : user_art})
    else:
        raise Http404('access denied!')

    
@login_required(login_url='login_view')
def curator_dashboard(request):
    arts_limit = Artwork.objects.all()[:5]
    if request.user.is_curator:
        return render(request, 'curator-dash.html', context={'curator': request.user, 'arts_limit' : arts_limit})
    else:
        raise Http404('access denied!')
    
    
@login_required(login_url='login')
def logout_func(request):
    logout(request)
    messages.success(request, 'logged out successfully!', extra_tags="success")

    return redirect('home_page')


def test(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            info = form.cleaned_data

            art_name = info['artwork_name']
            rating = info['rating']
            picture = info['picture']
            dec = info['description']

            Artwork.objects.create(artist=request.user, artwork_name=art_name, description=dec, rating=rating, picture=picture)

            return redirect('artwork_page')
        
        else:
            print(form.errors)
            return redirect('artist_dashboard')
        
    else:
        raise Http404
