from .views import *
from django.urls import path

urlpatterns = [
    path('',index),
    path('get-student/',get_student),
    path('add-student/',add_student),
]