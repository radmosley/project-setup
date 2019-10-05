from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('endpoints/', views.endPointsList.as_view()),
    path('endpoints/<int:pk>/', views.endPointsDetail.as_view())
]