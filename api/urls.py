from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_view, contact_success_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('portfolio', views.port, name='portfolio'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]

