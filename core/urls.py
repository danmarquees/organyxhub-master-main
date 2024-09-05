from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.index, name='index'),
    path('shop-details/', views.shop_details, name='shop-details'),
    path('shop-grid/', views.shop_grid, name='shop-grid'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
]