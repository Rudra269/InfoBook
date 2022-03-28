from django.contrib import admin
from .models import Livre


class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description')

admin.site.register(Livre,LivreAdmin)

# Register your models here.
