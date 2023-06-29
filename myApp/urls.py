
from .import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings  # Import settings module correctly


urlpatterns = [

    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('cart/success/', views.success),
    path('category/<int:category_id>/', views.category_page, name='category_page'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




