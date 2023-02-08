from .views import *
from django.urls import path

urlpatterns = [
    path('',index),
    path('get-student/',get_student),
    path('add-student/',add_student),
    path('patch-student/<int:id>/',patch_student),
    path('put-student/<int:id>/',put_student),
    path('delete-student/<int:id>/',delete_student),
    path('get-book/',get_book),
    path('student/',StudentView.as_view()),
]