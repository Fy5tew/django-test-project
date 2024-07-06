from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view),
    path('test/', views.test_view),
    path('url/', views.url_view),
]
