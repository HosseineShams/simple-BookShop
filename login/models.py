from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=50, verbose_name='Book', null=True, blank=True)
    author = models.CharField(max_length=25, verbose_name='Author', null=True, blank=True)
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='Date', null=True, blank=True)
    price = models.SmallIntegerField(verbose_name='Price',null=True, blank=True)
    category = models.ForeignKey('category', verbose_name='Category' ,on_delete=models.CASCADE, null=True, blank=True, related_name='book')
    quantity = models.SmallIntegerField(verbose_name='Quantity',null=True, blank=True)
    publication = models.CharField(max_length=50, verbose_name='Publication', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name='Categry', null=True, blank=True)

    def __str__(self):
        return self.name