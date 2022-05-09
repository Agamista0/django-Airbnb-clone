from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , CreateView
from django.views.generic.edit import FormMixin
from .models import Property , PropertyImages , PropertyReview , Category
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages



# Create your views here.

class PropertyList(ListView):
    model = Property 
    paginate_by = 2



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

