from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ineed-home'),
    path('about/', views.about, name='ineed-about'),
    path('providehelp/', views.providehelp, name='ineed-providehelp'),
    path('offerings/', views.offerings, name='ineed-offerings'),
    path('ineedthese/', views.ineedthese, name='ineed-these'),
]
