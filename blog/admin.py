from django.contrib import admin
from blog.models import Post, Story, Images


# Register your models here.
admin.site.register(Post)
admin.site.register(Story)
admin.site.register(Images)