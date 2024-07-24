from django.urls import path 
from . import views


urlpatterns = [
    path('',views.log_in,name="login"),
    path('test/',views.test_api,name="test"),
    path('home/',views.home,name="home"),
]