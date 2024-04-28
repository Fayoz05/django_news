from django.contrib import admin

from .models import CategoryModel, TextNews


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name','id']
    list_filter = ['created_at']
    list_display = ['id','category_name','created_at']
    ordering = ['id',]

@admin.register(TextNews)
class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['news_title','id','created_at']
    list_filter = ['created_at']
    list_display = ['id','news_title','created_at']
    ordering = ['id',]