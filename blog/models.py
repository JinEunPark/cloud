import os.path

from django.contrib.auth.models import User
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=30)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/',blank=True)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}] {self.title} , {self.author}' ##작성자 까지

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User,  null=True, on_delete=models.CASCADE) #장고의 기본 유저를 추가함 필수로 들어감
    # CASCAD 를 사용해서 유저가 삭제되면 글도 삭제됨

    def get_absolute_url(self):
        return  f'/blog/{self.pk}'

    def get_fileName(self):
        return os.path.basename(self.file_upload.name)
# Create your models here.
