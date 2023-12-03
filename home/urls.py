from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.statistics, name='statistics'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('model-explanation/', views.model_explanation, name='model'),
]
