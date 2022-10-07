from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('group/<slug:group_condition>/',views.group_posts),
]