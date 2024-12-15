from django.urls import path
from .import views

urlpatterns = [
    path("",views.homepage),
    path("home",views.homepage),
    path("about",views.aboutpage),
    path("contact",views.contactpage),
    path("form",views.frompage),
    path("process",views.frompageprocess),
    path("mark",views.subpage),
    path("sum",views.sumpage),
    path("add-student",views.addStudent),
    path("display-student",views.displayStudent),
    path("delete-student/<int:id>",views.deleteStudent,name='delete-student'),
    path("edit-student/<int:id>",views.editStudent),
]
