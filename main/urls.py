from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg.html', views.reg),
    path('cabinet.html', views.cabinet),
]
