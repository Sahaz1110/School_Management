from django.urls import path
from . import views

urlpatterns = [
    path('students/enroll/', views.enroll_student, name='enroll_student'),
    path('students/', views.student_list, name='student_list'),
]
