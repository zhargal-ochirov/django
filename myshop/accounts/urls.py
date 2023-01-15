from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_profile/', views.PersonCreateView.as_view(), name='edit_profile'),
    path('profile/', views.profile, name='profile')
]
