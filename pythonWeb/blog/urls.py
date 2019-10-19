from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList,name='blog'),
    path('<int:id>/', views.postNews, name='post_news')
]