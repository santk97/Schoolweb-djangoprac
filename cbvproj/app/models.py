from django.db import models
from django.urls import reverse

# Create your models here.
class Brand(models.Model):
    brandname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.brandname

    def get_absolute_url(self):
        return reverse("app:brand_detail",kwargs={'pk':self.pk})


class Product(models.Model):
    p_name=models.CharField(max_length=100)
    brand=models.ForeignKey(Brand,related_name='productbrand',on_delete=models.CASCADE)
    price=models.FloatField()

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse("app:product_detail", kwargs={'pk': self.pk})