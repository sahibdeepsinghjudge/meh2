from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.userData,name='api-all-users'),
    path('registers/',views.registerCount,name='api-all-registers'),
    path('<str:username>/',views.UserDetails,name='api-users-details'),
    path('location/<str:username>/',views.LocationDetails,name='api-location-details'),
    path('',views.api_wayback_machine,name='api')
]