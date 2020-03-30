from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, logout
from .models import Movie, Comment
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'streamer_app/home.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.date_joined = timezone.now()
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'streamer_app/signup.html', {'form': form})

def profile(request):
    movies = Movie.objects.all().order_by('-published_date')
    return render(request, 'streamer_app/profile.html', {'movies' : movies})

def movie_new(request):
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			movie = form.save(commit = False)
			movie.published_date = timezone.now()
			movie.save()
			return redirect('movie_detail', pk = movie.pk)
	else:
		form = MovieForm()
	return render(request, 'streamer_app/movie_edit.html', {'form' : form})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    comments = Comment.objects.filter (comment_on = movie).order_by('-published_date')
    return render(request, 'streamer_app/movie_detail.html', { 'movie' : movie, 'comments' : comments})