from django.contrib import admin
from .models import Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

admin.site.register(Genre,GenreAdmin)

# Register your models here.
