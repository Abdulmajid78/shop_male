from django.db import models


class BannerModel(models.Model):
    collection = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='banners/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class ContactMessageModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
