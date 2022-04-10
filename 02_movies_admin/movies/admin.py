from django.contrib import admin

from .models import Genre, Filmwork, GenreFilmwork, Person, PersonFilmWork


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmWork
    autocomplete_fields = ['person']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline,)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ['full_name']
    search_fields = ['full_name']
