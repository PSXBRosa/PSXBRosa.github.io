from . import views
from django.urls import path

urlpatterns = [
    path('', ... , name="index"),
    path('search/', ... , name='search'),
    path('subject/<slug:slug>/', ... , name="subject"),
    path('profile/<slug:slug>/', ... , name="profile"),
    path('auth/', ... , name="auth"),
    path('form/<slug:slug>', ... , name='form'),
]

