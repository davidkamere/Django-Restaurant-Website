from django.db import models


# Create your models here.
class Category(models.Model):
    main_category = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    extra_info = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return "%s" % self.main_category

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    sub_category = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    extra_info = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return "%s" % self.sub_category

    class Meta:
        verbose_name_plural = 'Sub Categories'


class Item(models.Model):
    main_category = models.ForeignKey(Category,
                                      on_delete=models.CASCADE, related_name='main_cat', blank=True, null=True)

    sub_category = models.ForeignKey(SubCategory,
                                     on_delete=models.CASCADE, related_name='sub_cat', blank=True, null=True)

    dish = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    extra_info = models.CharField(max_length=3000, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return "%s" % self.dish

    class Meta:
        verbose_name_plural = 'Items'
