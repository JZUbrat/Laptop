from django.db import models
from django.utils.text import slugify

# Create your models here.

class TimeStampelModelMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugifyModelMixins(models.Model):
    slug = models.SlugField(unique=True , blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand} {self.model}")
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
class Laptop(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=2000)
    cpu = models.CharField(max_length=2000)
    ozu = models.CharField(max_length=200)
    ssd = models.CharField(max_length=200)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='img', default='img/lenovo_legion_pro_5_Gen_8.jpg', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
