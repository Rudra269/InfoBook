from . import views
from django.urls import path
from .views import genre1

urlpatterns=[
    path('',views.index),
    path('genre1/', views.genre1),
    path('genre2/', views.genre2)
]