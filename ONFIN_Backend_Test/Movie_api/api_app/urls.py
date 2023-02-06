from django.urls import path
from .views import MovieCreateView, MovieDetailView, MovieListView


urlpatterns = [
    path('all_movies/',MovieListView.as_view()),
    path('add_movie/',MovieCreateView.as_view()),
    path('movie/<str:title>/',MovieDetailView.as_view()),
   
]