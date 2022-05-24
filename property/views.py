from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , CreateView
from django.views.generic.edit import FormMixin
from .models import Property , PropertyImages , PropertyReview , Category 
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages
from .filter import PropertyFilter
from django_filters.views import FilterView
from .models import Category
from blog.models import Post
from about.models import About
from django.contrib.auth.models import User
from django.db.models import Q 

# Create your views here.

class PropertyList(FilterView):
    
    model = Property 
    paginate_by = 4
    template_name = "property/property_list.html"
    filterset_class = PropertyFilter
    
    
    
def propertyByCategory (request,category):
    
    my_category=Category.objects.get(name=category)
    property_by_category=Property.objects.filter(category=my_category)
    return render(request,'property/property_by_category.html',{'property_by_category':property_by_category } )
    
    
    
    
class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name='property/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_post"] = Post.objects.all()[:4]
        context["property_Restaurants"] = Property.objects.filter(category__name='Restaurant')[:4]
        context["cv"] = About.objects.all()
        context["hotels"] = Property.objects.all()[:5]
        context["Places_count"] = Property.objects.filter(category__name= 'Places').count()
        context["Restaurant_count"] = Property.objects.filter(category__name= 'Restaurant').count()
        context["hotel_count"] = Property.objects.filter(category__name= 'Hotel').count()
        context["user_count"] = User.objects.all().count()
        
        return context
        
        




class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        context['get_related'] = Property.objects.filter(category=self.get_object().category)[:2]
        context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()


        return context


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.save()
        
   
            ### send gmail message

            return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))
    



class PropertyCreate(CreateView):
    model = Property
    fields = ['title','description','price','place','image','category']
    
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner=request.user
            myform.save()
            message.success(request,'successfuly added property ')
   
            ### send gmail message

        return redirect(reverse('property:property_list' ))
    
    
    
   

