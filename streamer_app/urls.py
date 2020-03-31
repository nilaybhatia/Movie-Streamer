from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/movies/new', views.movie_new, name='movie_new'),
    path('accounts/profile/movie/<int:pk>', views.movie_detail, name='movie_detail'),
    path('accounts/profile/movie/<int:pk>/comment/', views.comment_new, name='comment_new'),
    path('accounts/profile/movie/<int:pk>/delete', views.movie_delete, name='movie_delete'),
    path('accounts/profile/movie/<int:pk>/edit', views.movie_edit, name='movie_edit'),
]