from django.urls import path
from . import views




app_name = 'blog'


urlpatterns = [

    #image views
    path('', views.image_list, name='image_list'),


]

