from django.urls import path
from . import views

app_name = 'pr1'

urlpatterns = [
    path('', views.index, name='index'),
    path('music/<int:pk>/', views.MusicDetailView.as_view(),
         name='music_detail'),
    path('musics/', views.MusicListView.as_view(),
         name='music_list'),
    path('authors/', views.AuthorListView.as_view(),
         name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(),
         name='author_detail'),
    path('search/', views.search, name='search')
]