from django.urls import path
from .views import signup

urlpatterns = [
    path('signup/', view=signup, name='signup'),
]