from django.contrib import admin

# Register your models here.
from .models import Category, Post

class PostAdmin (admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['author']
    #search_fields = ['patient_name']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)