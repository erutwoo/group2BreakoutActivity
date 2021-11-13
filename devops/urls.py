from django.urls import path

from . import views

app_name = 'devops'
urlpatterns = [
    path('', views.index, name="index"),
    path('submit', views.submit, name="submit"),
    path('map', views.map, name="map")
]