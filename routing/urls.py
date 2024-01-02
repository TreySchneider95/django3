from django.urls import path
from routing import views

urlpatterns = [
    path('', views.home,name="home"),
    path('/display_name', views.display_name, name="display_name"),
    path('/favorite_food', views.display_food, name='food'),
    path('/vacation', views.display_vacation, name='vacation')
]