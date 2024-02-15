from django.urls import path
from . import views
urlpatterns=[
    path("home",views.home,name="home"),
    path("addStudent",views.addStudent,name="addStudent"),
    path("insertStudent",views.insertStudent,name="insertStudent"),
    path("contact",views.contact,name="contact"),
    path("viewStudent",views.viewStudents,name="viewStudent"),
    path("deleteStudent/<int:pk>",views.deleteStudent,name="deleteStudent"),
    path("updateStudent/<int:pk>", views.updateStudent, name="updateStudent"),
    path("index",views.index,name="index"),
    path("index1",views.index1,name="index1"),

]




