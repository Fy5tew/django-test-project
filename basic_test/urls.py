from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view),
    path('test/', views.test_view),
    path('avby/', views.avby_view),
    path('kufar/', views.kufar_view),
]
