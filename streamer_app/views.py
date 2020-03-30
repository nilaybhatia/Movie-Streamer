from django.shortcuts import render, redirect
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