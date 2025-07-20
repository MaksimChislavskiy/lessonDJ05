from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import HomePageView, ProfilePageView, RegisterPageView, CustomLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
]