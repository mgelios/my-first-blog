from django.contrib import admin
from .models import Post, Comment, Category, CategoryBundle

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(CategoryBundle)



