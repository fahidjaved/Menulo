from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = 'main'

urlpatterns = [

    path('recipies/<slug>/<id>', views.itemdetail2, name='recipies_id'),
    path('details/<slug>', views.itemdetail1, name='recipies'),
    path('', views.home, name='home'),
    path('restaurant/<slug>', views.resturent, name='restaurent'),
    path('impressum', views.impressum, name='impressum'),
    path('kontakt', views.Kontakt, name='kontakt'),
    path('agb', views.agb, name='agb'),
    path('login', views.login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('bestellen', views.bestellen, name='bestellen'),
    path('allgemein', views.allgemein, name='allgemein'),
    path('zusammenstellen', views.zusammenstellen, name='zusammenstellen'),
    path('speisekarte', views.speisekarte, name='speisekarte'),
    path('qr_code', views.qr_code, name='qr_code'),
    path('datenschutz', views.privacy, name='datenschutz'),
    path('so-funktioniert-es', views.funktioniert, name='so-funktioniert-es'),

    path('dashboard/prices', views.dashboard, name='dashboard'),
    path('dashboard/shisha', views.shisha, name='shisha'),
    path('dashboard/feedback', views.feedback, name='feedback'),
    path('dashboard/guests', views.guests, name='guests'),
]
