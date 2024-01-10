from django.urls import path
from .views import signup, login

urlpatterns = [
    path('signup/', view=signup, name='signup'),
    path('login/', view=login, name='login'),
]