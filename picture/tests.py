from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        '''Creating a new location and saving it'''
        self.loc1=Location(location="Mombasa")
        self.loc1.save_location()
        '''Creating a new category and saving it'''
        self.cat1=Category(category="food")
        self.cat1.save_category()
        '''Creating a new image and saving it'''
        self.img1=Image(image_name="scenery",image_description="an image test",location=self.loc1,category=self.cat1)
        self.img1.save()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

    '''
    test to save images
    '''
    def test_save_image(self):
        self.img1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    '''
    test to delete images
    '''
    def test_delete_images(self):
        self.img1.delete_image()
        deleted=Image.objects.all()
        self.assertEqual(len(deleted), 0)

    '''test to display images'''
    def test_display_images(self):
        all_images=Image.display_images()
        self.assertTrue(len(all_images)>0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.loc1=Location(location="Mombasa")

    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))

    def test_save_location(self):
        self.loc1.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1=Category(category="food")

    def test_instance(self):
        self.assertTrue(isinstance(self.cat1,Category))

    def test_save_category(self):
        self.cat1.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

