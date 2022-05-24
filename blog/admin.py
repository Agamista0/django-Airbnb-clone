from django.contrib import admin
from .models import Post , Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)

admin.site.register(Post ,PostAdmin)
admin.site.register(Category)