from django.contrib import admin
from blog.models import Post, Comment, Images, Subscription

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Subscription)
