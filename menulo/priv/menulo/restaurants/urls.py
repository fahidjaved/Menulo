from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'restaurants'

urlpatterns = [
    path('<slug>/', views.resturent, name='restaurent'),

]
