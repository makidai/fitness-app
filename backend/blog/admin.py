from django.contrib import admin
from blog.models import Category, Tag, Post, Collection, CollectionPost


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Collection)
admin.site.register(CollectionPost)