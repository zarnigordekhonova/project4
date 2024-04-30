from django.urls import path
from university_info.views import get_univer_info

urlpatterns = [
    path('', get_univer_info)
]