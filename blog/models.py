from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=30)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/',blank=True)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return  f'/blog/{self.pk}'
# Create your models here.
