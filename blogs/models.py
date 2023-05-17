from django.db import models
from ckeditor.fields import RichTextField
from users.models import UserModel


class BlogTagsModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    main_image = models.ImageField(upload_to='blogs/')
    banner_image = models.ImageField(upload_to='blogs/')
    tags = models.ManyToManyField(BlogTagsModel, related_name='blogs')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('-id',)


class CommentModel(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    comment = models.TextField()
    blog = models.ForeignKey(BlogModel, on_delete=models.RESTRICT, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
