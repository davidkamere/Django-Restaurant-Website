from django.db import models


# Create your models here.
class Post(models.Model):
    # category options
    CATEGORY_CHOICES = (
        (1, "News"),
        (2, "Recipe"),
        (3, "Other"),
    )

    back_story = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    ingredients = models.CharField(max_length=200, blank=True, null=True)
    recipe = models.CharField(max_length=500, blank=True, null=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=2)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)


class Images(models.Model):
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    back_story = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Images'




