from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def str(self):
        return self.name


class Article(models.Model):
    category = models.ManyToManyField(Category, related_name="items")
    title = models.CharField(max_length=100)
    thumb = models.ImageField(default='default.png', blank=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title





