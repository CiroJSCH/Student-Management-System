from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student/<int:id>", views.view_student, name="view_student"),
    path('add/', views.add_student, name='add_student')
]
