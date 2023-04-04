from django.contrib import admin
from blog.models import Post, Category

admin.site.register(Post)##DB로 만든 post class 를 가져옴

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} ##slug 필드 안에 카테고리 이름이 자동으로 삽입될 수있게 만들었음. 안녕하세요 박진은 입니다 잘부탇드립니다

admin.site.register(Category,CategoryAdmin)

# Register your models here.
