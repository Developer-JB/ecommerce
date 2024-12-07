from django.contrib import admin
from . models import Category,Product
# Register your models here.

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

 
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}



