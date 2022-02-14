from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.PostList, name='list'),   
]