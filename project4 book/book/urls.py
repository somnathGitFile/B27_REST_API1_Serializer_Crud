from django import views
from django.urls import path
from .views import BookView, BookInfo

urlpatterns = [
    path('bk/', BookView.as_view()),
    path('bk/<int:id>/', BookInfo.as_view())
]