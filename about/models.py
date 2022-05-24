
from django.db import models

# Create your models here.

class FAQ(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField(max_length=2000)
    class Meta:
        verbose_name = ("FAQ")
        verbose_name_plural = ("FAQ")

    def __str__(self):
        return self.title


class Footer (models.Model):
    
    name_website = models.CharField(max_length=25)
    description =models.TextField(max_length=2000)    
    twitter_url= models.URLField( max_length=200)
    facebook_url= models.URLField( max_length=200)
    instagram_url= models.URLField( max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    amail=models.EmailField( max_length=254)    

    class Meta:
        verbose_name = ("Footer ")
        verbose_name_plural = ("Footers")

    def __str__(self):
        return self.name_website
    
    
    
class About(models.Model):
    title1 = models.CharField(max_length=30)
    description1 = models.TextField(max_length=1000)
    title2 = models.CharField(max_length=30)
    description2 = models.TextField(max_length=1000)
    title3 = models.CharField(max_length=30)
    description3 = models.TextField(max_length=1000)
    title4 = models.CharField(max_length=30)
    description4= models.TextField(max_length=1000)
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("abouts")

    def __str__(self):
        return str(self.id)
    
    


   
