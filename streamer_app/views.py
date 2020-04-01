from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from django.contrib.auth import login, logout
from .models import Movie, Comment
from .forms import *
# Create your views here.

# The page that shows 2 option -- login/signup
def home(request):
    return render(request, 'streamer_app/home.html')

# For new user
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

# The all movies page displaying all movies
def profile(request):
    movies = Movie.objects.all().order_by('-published_datetime')
    return render(request, 'streamer_app/profile.html', {'movies': movies})

# View for adding a new movie by admin
@staff_member_required
def movie_new(request):
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.published_datetime = timezone.now()
			movie.save()
			return redirect('movie_detail', pk=movie.pk)
	else:
		form = MovieForm()
	return render(request, 'streamer_app/movie_edit.html', {'form': form})

# View for deleting a movie
@staff_member_required
def movie_delete(request, pk):
	movie = get_object_or_404(Movie, pk=pk).delete()
	return redirect('profile')

# View for editing a movie's title, link, etc.
@staff_member_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.published_date = timezone.now()
            movie.save()
            return redirect('movie_detail', pk = movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'streamer_app/movie_edit.html', {'form': form})


# The view for displaying details of a movie
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = Comment.objects.filter(
        comment_on=movie).order_by('-published_datetime')
    return render(request, 'streamer_app/movie_detail.html', {'movie': movie, 'comments': comments})

# View for adding a new comment
def comment_new(request, pk):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.published_date = timezone.now()
			movie = get_object_or_404(Movie, pk = pk)
			comment.comment_on = movie
			comment.author = request.user
			comment.save()
			return redirect('movie_detail', pk = movie.pk)
	else:
		form = CommentForm()
		movie = get_object_or_404(Movie, pk = pk)
	return render(request, 'streamer_app/comment_edit.html', {'form':form, 'movie' : movie})

