from django.urls import path
from . import views
from . import api_views


app_name = 'property'


urlpatterns = [
    path( '',views.CategoryList.as_view() , name='home' ),
    path( 'property/list',views.PropertyList.as_view() , name='property_list' ),
    path( 'property/new',views.PropertyCreate.as_view() , name='property_new' ),
    path('property/<slug:slug>',views.PropertyDetail.as_view() , name='property_detail'),
    path('property/category/<str:category>',views.propertyByCategory , name='property_by_category'),

    
    path('property/api/list',api_views.propertyListApi.as_view(),name="property_list_api"),
    path('property/api/list/<int:pk>',api_views.propertyDetailApi.as_view(),name="property_detail_api"),
]
