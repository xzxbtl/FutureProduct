from . import views
from django.urls import path


app_name = 'catalog'

urlpatterns = [
    path('', views.main, name="main"),
    path('product/<slug:product_slug>/', views.product, name="product"),
    path('product/client-wish', views.upload_photo, name="wish")
]