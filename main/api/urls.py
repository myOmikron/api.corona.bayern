from django.urls import path
from api import views

urlpatterns = [
    path('refresh/', views.RefreshView.as_view()),
    path('getCounties/', views.GetCountiesView.as_view()),
    path('getLatestData/', views.GetLatestData.as_view()),
]
