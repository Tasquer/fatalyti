from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_app1, name='index_app1'),
]