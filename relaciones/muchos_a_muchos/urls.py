from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='muchos_a_muchos_index'),
]
