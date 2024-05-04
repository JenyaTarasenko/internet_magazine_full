from django.db import models
from django.urls import reverse

class Category(models.Model):
    """ модель категорий товара"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ модель товара"""
    category = models.ForeignKey(Category,
                                 related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        """ Абсолютный  url для product"""
        return reverse('shop:product_detail',
                       args=[self.id, self.slug]
                       )


class Contact(models.Model):
    """Модель формы """
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.email




