from django.urls import path
from .views import apiHome, UserView
from . import views

urlpatterns = [
    path('', apiHome),
    path('user/', UserView.as_view()),

    path('signup/', views.signupPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    
]