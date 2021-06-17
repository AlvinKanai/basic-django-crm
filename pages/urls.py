from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import LandingPageView, SignUpView

app_name = 'pages'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
