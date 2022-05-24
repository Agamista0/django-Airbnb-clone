from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE, verbose_name= _("outher"))
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),max_length=12000)
    price = models.IntegerField(_('price'))
    place = models.CharField(_('place'),max_length=50)
    image = models.ImageField(_('image'),upload_to='propery/')
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE , verbose_name= _("category"))   
    slug = models.SlugField(_('slug'),blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'),auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('Properties')

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property:property_detail' , kwargs={'slug':self.slug})



class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(_("image"),upload_to='property_images/')

    def __str__(self):
        return self.property.title


    class Meta:
        verbose_name = _('Property Image')
        verbose_name_plural = _('Property Images')



class Category(models.Model):
    name = models.CharField(_("name"),max_length=25)
    icon  = models.CharField(max_length=30,blank=True, null=True)

    class Meta:
        verbose_name = _("PropertyBook")
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name





class PropertyReview(models.Model):
    property = models.ForeignKey(Property, related_name='property_review', on_delete=models.CASCADE, verbose_name = _("property"))
    author = models.ForeignKey(User, related_name='review_owner', on_delete=models.CASCADE, verbose_name = _("author"))
    rating = models.PositiveIntegerField(_("rating"),default=0 ,  validators=[MaxValueValidator(5)])
    feedback = models.TextField(_("feedback"),default='' , max_length=200)


    def __str__(self):
        return self.property.title
    
    
    class Meta:
        verbose_name = _("PropertyReview")
        verbose_name_plural = _('PropertyReviews')

PEOPLE_TYPE = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)



class PropertyBook(models.Model):
    property = models.ForeignKey(Property, related_name='property_book', on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name='user_book', on_delete=models.CASCADE)
    date_from = models.DateField( _("date_from"),default=timezone.now)
    date_to =  models.DateField( _("date_to"),default=timezone.now)
    guest = models.IntegerField(_("guest"), default=1 , choices=PEOPLE_TYPE)
    children = models.IntegerField( _("children"),default=0 , choices=PEOPLE_TYPE)


    def __str__(self):
        return self.property.title
    
    class Meta:
        verbose_name = _("PropertyBook")
        verbose_name_plural = _('PropertyBooks')