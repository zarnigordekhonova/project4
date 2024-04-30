from django.urls import path
from students.views import get_student_info

urlpatterns = [
    path('', get_student_info)
]