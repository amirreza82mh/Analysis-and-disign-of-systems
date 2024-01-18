from django.urls import path
from .views import signupview, loginview

urlpatterns = [
    path('signup/', view=signupview, name='signup_view'),
    path('login/', view=loginview, name='login_view'),
]