from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='abo'),
    path('create', views.create, name='create'),
]
