from django.urls import path
from api import views

urlpatterns = [

    path('school/', views.ProfileView.as_view(), name='school'),
    path('list/', views.ProfileView.as_view(), name='list'),

]
