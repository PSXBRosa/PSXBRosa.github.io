from . import views
from django.urls import path

urlpatterns = [
    path('', views.index , name="index"),
    path('search/', views.DisciplinaListView.as_view() , name='search'),
    path('subject/<slug:slug>/', views.DisciplinaDetailView , name="subject"),
    path('login/', views.login, name="login"),
    # path('profile/<slug:slug>/', ... , name="profile"),
    # path('auth/', ... , name="auth"),
    # path('form/<slug:slug>', ... , name='form'),
]

