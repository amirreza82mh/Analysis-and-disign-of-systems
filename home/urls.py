from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('artwork_detail/<int:id>', view=views.artwork_detail, name='artwork_detail'),
    path('reserve_ticket/<int:id>', view=views.reserve_ticket, name='exhibition_detail'),
    path('artworks/', view=views.artwork_page, name="artwork_page"),
    path('about_us/', view=views.about_us, name="about_us_page"),
    path('contact_us/', view=views.contact_us, name="contact_us_page"),
]