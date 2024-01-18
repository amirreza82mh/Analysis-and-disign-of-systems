from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

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

            if user is not None:
                login(request=request, user=user)
                messages.success(request, 'login successfull', extra_tags="succuss")
                return redirect('index')
            
            else:
                messages.error(request, 'invalid credentials', extra_tags="danger")
                return redirect('login_view')
            
        else:
            messages.error(request, 'form is not valid', extra_tags="danger")
            return redirect('login_view')

    else:
        form = LoginForm(request.POST)
    
    return render(request, 'login.html', context={'form': form})