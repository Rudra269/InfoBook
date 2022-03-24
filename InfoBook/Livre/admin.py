from django.contrib import admin
from .models import Livre

class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'descrption')


admin.site.register(Livre, LivreAdmin)
