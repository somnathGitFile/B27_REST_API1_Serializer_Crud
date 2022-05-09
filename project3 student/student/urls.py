from django.urls import path
from . import views


urlpatterns = [
    path('stu/', views.StudentDetails.as_view()),
    path('stu/<int:id>/', views.StudentInfo.as_view())
]