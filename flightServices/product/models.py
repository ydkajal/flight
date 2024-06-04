from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
