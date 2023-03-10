from django.urls import path

from .views import post_details, category_detail, search

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', post_details, name='post_details'),
    path('<slug:slug>/', category_detail, name='category_details'),
]
