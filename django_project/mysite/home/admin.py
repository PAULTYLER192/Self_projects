from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created_at')
  search_fields = ('title', 'content')
  list_filter = ('title', 'created_at')
  
admin.site.register(Post, PostAdmin)