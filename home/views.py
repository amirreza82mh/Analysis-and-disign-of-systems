from django.shortcuts import render

def home_page(request):
    return render(request, 'Home.html')

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')