from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from .models import User
from django.template import loader
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            if info['password1'] != info['password2']:
                messages.error(request, 'please enter same password in field confirmpassword', extra_tags="daner")
                return redirect('signup')
                        
            try:
                info[request.POST.get('type')] = True
                User.objects.create(username=info['username'], email=info['email'], phone_number=info['phone_number'], password=info['password1'], is_curator=info['is_curator'], is_artist=info['is_artist'], is_viewer=info['is_viewer'])
                messages.success(request, 'User successfully SignUp', extra_tags="success")
                return redirect('admin')
            
            except Exception as error:
                messages.error(request, error, extra_tags="danger")
                return render(request, 'login.html')
            
        else:
            print(form.errors)
            messages.error(request, form.errors, extra_tags="danger")
            return redirect('signup')
        
    else:
        form = SignUpForm()

    return render(request, 'login.html', context={"form": form})


def login(request):
    pass