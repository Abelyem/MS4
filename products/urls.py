from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<mask_id>', views.mask_detail, name="mask_detail"),
]
