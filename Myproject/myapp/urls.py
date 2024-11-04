from django.urls import path
 
from . import views

urlpatterns = [
    path('analyze/', views.analyze_playlist_comments, name='analyze_playlist_comments'),
 
     
]