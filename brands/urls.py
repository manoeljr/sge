from django.urls import path

from .views import BrandListView


urlpatterns = [
    path('brand/list/', BrandListView.as_view(), name='brand_list'),
]
