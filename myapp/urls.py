from django.urls import path
from .import views

urlpatterns = [
    path("",views.homepage),
    path("about",views.aboutpage),
    path("contact",views.contactpage),
]
