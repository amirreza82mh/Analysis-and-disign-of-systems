from django.urls import path
from .views import signupview, loginview, viewer_dashboard, artist_dashboard, curator_dashboard, logout_func, select_dash

urlpatterns = [
    path('signup/', view=signupview, name='signup_view'),
    path('login/', view=loginview, name='login_view'),
    path('viewr/dashboard', view=viewer_dashboard, name='viewer_dashboard'),
    path('artsit/dashboard', view=artist_dashboard, name='artist_dashboard'),
    path('curator/dashboard', view=curator_dashboard, name='curator_dashboard'),
    path('logout/', view=logout_func, name='logout'),
    path('show_dashboard/', view=select_dash, name='show_dashboard')
]