from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('contact/', view=views.contact_us, name='contact'),
    path('about_us/', view=views.about_us, name='about us'),
    path('artwork_detail/<int:id>', view=views.artwork_detail, name='artwork_detail')
]