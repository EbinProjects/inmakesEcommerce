from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'myapp'  # This must match the namespace used in your template
urlpatterns = [

    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:producr_slug>/', views.allProductDetails, name='productCatDetails')
    # Other URLs
]
