from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='Product',on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=50)
    brand=models.CharField(max_length=500 , default='un-branded')
    description=models.TextField(blank=True)
    slug = models.SlugField(max_length=50,unique=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(blank=True,upload_to='images/')

    class Meta:
        verbose_name_plural ='Products'

    def __str__(self):
        return self.title
    