from django.db import models
import datetime as dt

# Create your models here.



class Image(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    posted_date= models.DateTimeField(auto_now_add=True)
    category_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['first_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    @classmethod
    def search_by_category(cls,search_term):
        portfolio = cls.objects.filter(category__name__icontains=search_term)
        return portfolio

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        img_id = cls.objects.get(pk=id)
        return img_id
