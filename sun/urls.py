from django.urls import path

from . import views

app_name = "sun"
urlpatterns = [
    path('', views.home, name="home")
]