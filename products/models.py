from django.db import models
from django.utils import timezone


class ProductBrandModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

class ProductSizeModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductColorModel(models.Model):
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'code'
        verbose_name_plural = 'codes'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    discount = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    color = models.ManyToManyField(ProductColorModel, related_name='products')
    size = models.ManyToManyField(ProductSizeModel, related_name='products')
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def real_price(self):
    #     if self.discount:
    #         return self.price - (self.price * self.discount) / 100
    #     return self.price

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)
