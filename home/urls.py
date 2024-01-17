from django.urls import path
from . import views

urlpatterns = [
    path('contact/', view=views.contact_us, name='contact'),
    path('about_us/', view=views.about_us, name='about us')
]