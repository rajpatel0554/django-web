from django.urls import path
from .import views

urlpatterns = [
    path("",views.demopage),
    path("home",views.homepage),
    path("about",views.aboutpage),
    path("contact",views.contactpage),
    path("form",views.frompage),
    path("process",views.frompageprocess),
    path("mark",views.subpage),
    path("sum",views.sumpage),
]
