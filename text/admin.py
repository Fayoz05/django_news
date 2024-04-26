from django.contrib import admin

from .models import CategoryModel, News


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name','id']
    list_filter = ['created_at']
    list_display = ['id','category_name','created_at']
    ordering = ['id',]

admin.site.register(News)