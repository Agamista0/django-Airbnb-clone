from django.urls import path
from . import views
from . import api_Views

app_name= "about"
urlpatterns = [
    path("",views.aboutList.as_view(),name="about_list"),
    
    # api 
    path("api/list",api_Views.faq_api_view.as_view(),name="about_fqa_api"),
    path("api/about",api_Views.about_api_view,name="about_list_api"), 

]
