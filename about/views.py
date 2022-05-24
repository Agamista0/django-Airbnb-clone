from django.shortcuts import render
from django.views.generic import ListView 
from .models import About ,Footer ,FAQ

# Create your views here.


class aboutList(ListView):
    model = FAQ 
    template_name ="about/about_list.html"
    context_object_name = "about_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cv"] = About.objects.all()
        return context
    