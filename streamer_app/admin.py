from django.contrib import admin
from .models import Movie, Comment
# Register your models here.
app_models = [Movie, Comment]
admin.site.register(app_models)