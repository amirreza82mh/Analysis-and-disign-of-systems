from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('artwork_detail/<int:id>', view=views.artwork_detail, name='artwork_detail'),
    path('exhibition_detail/<int:id>', view=views.exhibition_detail, name='exhibition_detail'),
    path('artworks', view=views.artwork_page, name="artwork_page"),
]