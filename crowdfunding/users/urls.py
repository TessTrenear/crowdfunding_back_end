from django.urls import path
from . import views # . means import the views from this file. Tell code how to traverse folders.

urlpatterns = [
    path('users/' , views.CustomeUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view())
]