from django.shortcuts import render
from .models import Post , Category
from django.views.generic import ListView , DetailView
from taggit.models import Tag
from django.db.models import Count ,Q


# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 6
     
    def get_queryset(self):
        name = self.request.GET.get('q','')
        abject_list = Post.objects.filter(
            Q(title__icontains=name) |  
            Q(description__icontains=name)
        )
        return  abject_list
    

   
   
class PostDetail(DetailView):
    model = Post
    
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blog"] = Post.objects.all()[:3]
        context["tags"] = Tag.objects.all()
        context["categories"]= Category.objects.all().annotate(post_count=Count("post_category"))

        
        return context
    
