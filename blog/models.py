from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    # category options
    CATEGORY_CHOICES = (
        (1, "News"),
        (2, "Recipe"),
        (3, "Other"),
    )

    content = RichTextUploadingField()
    title = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    extra_info = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    serving = models.TextField(blank=True, null=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=2)
    header_image = models.ImageField(upload_to='images/', blank=False, null=False)
    slug = models.SlugField()


    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

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


class Subscription(models.Model):
    """Stores subscribers"""
    address = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Email Addresses'

    def __str__(self):
        return self.address




