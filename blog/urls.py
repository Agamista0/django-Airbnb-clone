from django.urls import path 
from . import views
from . import  api_view


app_name ="blog"
urlpatterns = [
    path('',views.PostList.as_view(),name="blog_list"),
    path('<slug:slug>',views.PostDetail.as_view(),name="blog_detail"),

    path('api/list', api_view.Post_list_api ,name="blog_list_api"),
    path('api/list/<int:id>', api_view.Post_detail_api ,name="blog_detail_api"),
]