from django.contrib import admin
from .models import Category,Location,Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
  

admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)
