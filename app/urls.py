from . import views
from django.urls import path

urlpatterns = [
    path('', views.index , name="index"),
    path('search/', views.DisciplinaListView.as_view() , name='search'),
    path('subject/<slug:slug>/', views.DisciplinaDetailView.as_view() , name="subject"),
    path('about/', views.about, name="about"),
    path('contato/', views.contato, name="contato"),
    # path('profile/<slug:slug>/', ... , name="profile"),
    path('avaliacao/<slug:slug>', views.create_avaliacao , name='avaliacao'),
    path('myprofile/', views.my_profile, name='my_profile')
]