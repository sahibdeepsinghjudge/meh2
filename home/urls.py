from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/search/',views.search,name='search'),
    path('home/search/items/',views.basicSearch,name='basic-search'),
]