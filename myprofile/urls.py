from django.urls import path
from . import views

app_name = "myprofile"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path('gallery/', views.gallery, name='gallery'),
]



