from django.contrib import admin
from .models import FAQ ,Footer , About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


class aboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ['description','description1','description2','description3','description4']




admin.site.register(FAQ ,aboutAdmin )
admin.site.register(Footer ,aboutAdmin)
admin.site.register(About ,aboutAdmin)