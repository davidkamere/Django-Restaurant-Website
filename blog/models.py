from django.db import models


# Create your models here.
class Story(models.Model):
    story = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "%s" % self.story[:30]

    class Meta:
        verbose_name_plural = 'Stories'


class Images(models.Model):
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    back_story = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Images'


class Post(models.Model):
    back_story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='back_story', blank=True, null=True)
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    recipe = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name_plural = 'Posts'

