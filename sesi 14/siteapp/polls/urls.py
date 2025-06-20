from django.urls import path
from . import views

urlpatterns = [
    path('alamat', views.alamat_view, name='alamat'),
    path('telepon', views.telepon_view, name='telepon'),
]


