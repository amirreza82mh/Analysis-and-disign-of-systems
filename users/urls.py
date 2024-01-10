from django.urls import path
from .views import signupview, loginview, index

urlpatterns = [
    path('index/', view=index, name='index'),
    path('signup/', view=signupview, name='signup_view'),
    path('login/', view=loginview, name='login_view'),
]