from django.db import models
from django.utils.text import slugify


# from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=155)

    mainCategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                     help_text="Eğer bu kategori başka bir kategoriye bağlıysa burayı doldurunuz")  # self kullanma nedenimiz bir kategori diğer kategorinin üst kategorisi olabilir.
    isActive = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, blank=True, null=True, unique=True)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brands/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Brands'
        verbose_name = 'Brand'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=155)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Türk Lirası cinsinden giriniz')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, blank=True, null=True, unique=True)
    isActive = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    main_window_display = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)
        return self.slug


class Variations(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    parent_variant = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Türk Lirası cinsinden giriniz')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='variations/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Variations'
        verbose_name = 'Variation'

    def __str__(self):
        return f"{self.product.name} - {self.name}"
