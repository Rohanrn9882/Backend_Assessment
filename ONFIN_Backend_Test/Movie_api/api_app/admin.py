from django.contrib import admin
from .models import Movie

# Register your models here.
# class GenreAdmin(admin.ModelAdmin):
#     list_display = ['name']

# admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'genre', 'uuid']

admin.site.register(Movie, MovieAdmin)