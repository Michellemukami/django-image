

from django.db import models
import datetime as dt


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_Category(self):
        self.save()
    

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    category = models.ForeignKey(Category)
    Location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    Pixels_image = models.ImageField(upload_to = 'pixels/', blank=True)
   
    @classmethod
    def location(cls):
        pixels = cls.objects.all()
        return pixels
    @classmethod
    def search_by_cat(cls, search_term):
        pixels=cls.objects.filter(category__icontains=search_term)
        return pixels
