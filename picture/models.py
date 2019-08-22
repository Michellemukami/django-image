

from django.db import models
import datetime as dt


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
   

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    @classmethod
    def location(cls):
        today = dt.date.today()
        pixels = cls.objects.filter(name = name)
        return pixels

  

class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    category = models.ForeignKey(Category)
    Location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    Pixels_image = models.ImageField(upload_to = 'pixels/', blank=True)
   
    @classmethod
    def search_by_category(cls,search_term):
        pixel = cls.objects.filter(category__icontains=search_term)
        return pixel
        