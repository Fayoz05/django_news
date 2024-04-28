from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class TextNews(models.Model):
    news_title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.TextField(default='')
    image = models.FileField(upload_to='news_images')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



