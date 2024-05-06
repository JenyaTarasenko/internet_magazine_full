from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    
    path('', views.ProductListView.as_view(), name='product_list'),#first page
    path('<int:id>/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),#detail page
    path('category/<slug:category_slug>/', views.ProductByCategory.as_view(), name='product-list-by-category'),#category page
    path('all-categories/', views.AllCategoryView.as_view(), name="all-by-category"),#all category page
    path('search/', views.ProductSearchListView.as_view(), name='product-search'),#search page
    # path('form/', views.contact_view, name='contact-form'),#form page   
]