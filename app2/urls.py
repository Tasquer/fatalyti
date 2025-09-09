from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_app2, name='index_app2'),
]