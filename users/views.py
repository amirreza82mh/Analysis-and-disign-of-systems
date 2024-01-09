from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from .models import User
from django.template import loader
from django.contrib import messages

def is_valid_rule(info):
    validate = (
        (info['is_artist'] == True and info['is_viewer'] == False and info['is_curator'] == False) or
        (info['is_artist'] == False and info['is_viewer'] == True and info['is_curator'] == False) or
        (info['is_artist'] == False and info['is_viewer'] == False and info['is_curator'] == True)
    )

    return validate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            if info['password1'] != info['password2']:
                messages.error(request, 'please enter same password in field confirmpassword', extra_tags="daner")
                return HttpResponseRedirect('/user/signup/')
            if is_valid_rule(info) == False:
                messages.error(request, 'can not choice more rule', extra_tags="daner")
                return HttpResponseRedirect('/user/signup/')
            try:
                form.save()
                messages.success(request, 'User successfully SignUp', extra_tags="success")
                return HttpResponseRedirect('/admin/')
            except Exception as error:
                messages.error(request, error, extra_tags="danger")
                return HttpResponse('/user/signup/')
        else:
            messages.error(request, form.errors, extra_tags="danger")
            return HttpResponseRedirect('user/signup/')
    else:
        form = SignUpForm()

    template = loader.get_template('test.html')
    return HttpResponse(template.render(context={'form': form}, request=request))