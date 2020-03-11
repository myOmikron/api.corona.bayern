from django.urls import path
from api import views

urlpatterns = [
    path('refresh/', views.RefreshView.as_view()),
]
