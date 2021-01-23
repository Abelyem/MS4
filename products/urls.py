from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:mask_id>', views.mask_detail, name="mask_detail"),
]
